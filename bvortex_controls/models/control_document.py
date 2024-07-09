import datetime

from odoo import api, fields, models, exceptions, _

class control_document(models.Model):
    _name = 'control.document'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char('Code', readonly=True)
    name = fields.Char('Name')
    partner_id = fields.Many2one('res.partner', string="Customer", domain=[('is_company', '=', True)])
    reception_date = fields.Date('Reception Date')
    deadline = fields.Date('Deadline')
    minister_id = fields.Many2one('control.minister', string="Minister")
    project_id = fields.Many2one('project.project', string="Project")
    nature_id = fields.Many2one('control.nature', string="Nature")
    reference = fields.Char('Reference')
    task_ids = fields.One2many('project.task', 'document_id', string="Tasks")
    action_ids = fields.Many2many('control.action', string="Actions")
    user_ids = fields.Many2many('res.users', string="Assignees")
    category = fields.Selection(selection=[
        ('spontanne', 'Contrôle Spontanné'),
        ('fiscal', 'Contrôle Fiscal'),
        ('parafiscal', 'Parafiscalité'),
    ], string='Category', required=True, default='spontanne')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')
    task_count = fields.Integer(compute='task_compute_count')
    day_count = fields.Integer(compute='deadline_compute_count')

    def get_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'tree,form',
            'res_model': 'project.task',
            'domain': [('id', '=', self.task_ids.ids)],
            'context': {
                'create': False,
                'default_partner_id': self.partner_id.id,
                'default_document_id': self.id,
            }
        }
    def task_compute_count(self):
        for record in self:
            record.task_count = self.env['project.task'].search_count([('id', '=', self.task_ids.ids)])

    def deadline_compute_count(self):
        for record in self:
            if record.deadline:
                difference = record.deadline - datetime.date.today()
                record.day_count = difference.days
            else:
                record.day_count = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('control.document') or 'DOC'
            msg_body = 'Control Document Created'
            for msg in self:
                msg.message_post(body=msg_body)
            result = super(control_document, self).create(vals_list)
        return result

    def action_confirmed(self):
        for rec in self:
            users = self.env['res.groups'].search([('id', '=', self.env.ref('bvortex_controls.group_fiscal_manager').id)]).users
            if not users:
                raise exceptions.UserError(
                    _("No users in the group Fiscal Manager !!"))

            activity_type = self.env.ref('bvortex_controls.mail_act_document')

            for user in users:
                self.activity_schedule(activity_type_id=activity_type.id, user_id=user.id,
                                       note=f'Please check this document for the customer {self.partner_id.name}')
            rec.state = 'confirmed'
            message = _(f'Confirmed Document !!')
            user = rec.env.user.sudo()

            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': message,
                    'img_url': '/web/image/%s/%s/image_1024' % (
                        user._name, user.id) if user.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }

    def action_in_progress(self):
        for rec in self:
            activity_id = self.env['mail.activity'].search(
                [('res_id', '=', rec.id), ('user_id', '=', rec.env.user.id),
                 ('activity_type_id', '=', rec.env.ref('bvortex_controls.mail_act_document').id)]
            )
            activity_id.action_feedback(feedback="Control Document validated")
            other_activity_ids = rec.env['mail.activity'].search(
                [('res_id', '=', rec.id),
                 ('activity_type_id', '=', rec.env.ref('bvortex_controls.mail_act_document').id)]
            )
            other_activity_ids.unlink()

            deadline = datetime.timedelta(days=rec.minister_id.deadline)
            rec.deadline = datetime.date.today() + deadline

            users = rec.env['res.groups'].search(
                [('id', '=', rec.env.ref('bvortex_controls.group_fiscal_manager').id)]).users

            project_id = rec.env['project.project'].search([('partner_id', '=', rec.partner_id.id), ('is_fiscal_project', '=', True)])

            if not project_id:
                vals = {
                    'name': f'{str(rec.partner_id.name).upper()}-[DOSSIER]',
                    'user_id': users[0].id if users else False,
                    'partner_id': rec.partner_id.id,
                    'is_fiscal_project': True,
                }

                project_id = rec.env['project.project'].create(vals)

                project_id.write({
                    'type_ids': [(4, rec.env.ref('bvortex_controls.draft_stage').id)],
                })

                project_id.write({
                    'type_ids': [(4, rec.env.ref('bvortex_controls.in_progress_stage').id)],
                })

                project_id.write({
                    'type_ids': [(4, rec.env.ref('bvortex_controls.concluded_stage').id)],
                })

                project_id.write({
                    'type_ids': [(4, rec.env.ref('bvortex_controls.cancelled_stage').id)],
                })


            for i in range(len(rec.action_ids)):
                vals = {
                    'name': f'{rec.action_ids[i].name}-{rec.name}',
                    'project_id': project_id.id,
                    'partner_id': rec.partner_id.id,
                    'user_ids': [(6, 0, [rec.user_ids[i].id])],
                    'document_id': rec.id,
                    'date_deadline': rec.deadline,
                }

                task_id = rec.env['project.task'].create(vals)

                task_id.write(
                    {
                        "tag_ids": [(4, rec.minister_id.tag_id.id)],
                    }
                )

                rec.task_ids.write(
                    {
                        "tag_ids": [(4, rec.nature_id.tag_id.id)],
                    }
                )

            rec.state = 'in_progress'

            message = _(f'Validated Document !!')
            user = rec.env.user.sudo()

            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': message,
                    'img_url': '/web/image/%s/%s/image_1024' % (
                        user._name, user.id) if user.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }

    def action_cancel(self):
        for rec in self:
            activity_id = self.env['mail.activity'].search(
                [('res_id', '=', self.id), ('user_id', '=', self.env.user.id),
                 ('activity_type_id', '=', self.env.ref('bvortex_controls.mail_act_document').id)]
            )
            activity_id.action_feedback(feedback="Control Document cancelled")
            other_activity_ids = self.env['mail.activity'].search(
                [('res_id', '=', self.id),
                 ('activity_type_id', '=', self.env.ref('bvortex_controls.mail_act_document').id)]
            )
            other_activity_ids.unlink()
            rec.state = 'cancel'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'