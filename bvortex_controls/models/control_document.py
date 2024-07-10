import datetime
import re

from odoo import api, fields, models, exceptions, _

class control_document(models.Model):
    _name = 'control.document'
    _description = 'Control Document'
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
    user_id = fields.Many2one('res.users', 'Login User', readonly=True, default=lambda self: self.env.user)
    out_of_time = fields.Boolean(default=False)
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self.env.company.currency_id)
    on_time = fields.Boolean(default=False)
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
    compute_situation = fields.Boolean(compute='_compute_situation')

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
            record.task_count = record.env['project.task'].search_count([('id', '=', record.task_ids.ids)])

    @api.depends('deadline', 'state')
    def _compute_situation(self):
        for rec in self:
            if rec.deadline:
                if rec.state in ['confirmed','in_progress']:
                    if rec.deadline >= datetime.date.today():
                        rec.out_of_time = False
                        rec.on_time = True
                    elif datetime.date.today() > rec.deadline:
                        rec.out_of_time = True
                        rec.on_time = False

                rec.compute_situation = True
            else:
                rec.compute_situation = False


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
    def get_fiscal_manager_user(self):
        fiscal_manager = self.env['res.groups'].search(
            [('id', '=', self.env.ref('bvortex_controls.group_department_head').id)], limit=1).users
        return fiscal_manager
    def get_emails_for_department_head(self):
        users = self.env['res.groups'].search(
            [('id', '=', self.env.ref('bvortex_controls.group_department_head').id)]).users
        return ','.join(users.mapped('email'))

    def is_valid_email(self, email):
        """Validate the email address using regex."""
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(email_regex, email):
            return True
        return False
    def get_category(self):
        for rec in self:
            if rec.category == 'spontanne':
                return 'Contrôle Spontanné'
            if rec.category == 'fiscal':
                return 'Contrôle Fiscal'
            if rec.category == 'parafiscal':
                return 'Parafiscalité'


    def action_confirmed(self):
        for rec in self:
            users = self.env['res.groups'].search([('id', '=', self.env.ref('bvortex_controls.group_fiscal_manager').id)]).users
            if not users:
                raise exceptions.UserError(
                    _("No users in the group Fiscal Manager !!"))

            if not rec.user_id.email:
                raise exceptions.UserError(
                    _("Your email is empty !!"))

            if not rec.get_fiscal_manager_user().email:
                raise exceptions.UserError(
                    _("The Fiscal Manager email is empty !!"))


            if rec.user_id.email:
                if not rec.is_valid_email(rec.user_id.email):
                    raise exceptions.UserError(
                        _("Your email is not valid !!"))

            if rec.get_fiscal_manager_user().email:
                if not rec.is_valid_email(rec.get_fiscal_manager_user().email):
                    raise exceptions.UserError(
                        _("The Fiscal Manager email is not valid !!"))

            activity_type = self.env.ref('bvortex_controls.mail_act_document')

            for user in users:
                self.activity_schedule(activity_type_id=activity_type.id, user_id=user.id,
                                       note=f'Please check this document for the customer {self.partner_id.name}')

            deadline = datetime.timedelta(days=rec.minister_id.deadline)
            rec.deadline = datetime.date.today() + deadline
            email_body = """
                <html>
                    <head>
                        <style>
                            table {
                                border-collapse: collapse;
                                width: 100%;
                            }
                            th, td {
                                text-align: left;
                                padding: 8px;
                                border-bottom: 1px solid #ddd;
                            }
                        </style>
                    </head>
                    <body>
                        <div style="margin: 0px; padding: 0px;">
                            <p style="margin: 0px; padding: 0px; font-size: 13px;">
            """
            email_body += f"""Bonjour <b>Mr {rec.get_fiscal_manager_user().name}</b>,<br/>"""
            email_body += """Chers collaborateurs en copie<br/><br/>"""
            email_body += f"""Je vous prie de trouver en annexe le document sur le (la) : <b>{rec.nature_id.name}</b> issu du (la) <b>{rec.minister_id.name}</b><br/>"""
            email_body += f"""pour un montant de <b>{rec.currency_id.name}</b> <b>{rec.amount}</b> dans le cadre du <b>{rec.get_category()}</b> pour compte du client <b>{rec.partner_id.name}</b><br/>"""
            email_body += f"""dont l'échéance de traitement est de <b>{rec.day_count} jours</b><br/>
                        <br/>
                        <br/>"""
            email_body += """Merci pour votre diligence quant au traitement ce dossier
                        <br/>Cordialement,<br></br>"""
            email_body += f"""<i><b>{rec.env.user.name}</b></i>"""
            email_body += """
                            </p>
                        </div>
                    </body>
                </html>
            """

            mail_vals = {
                'email_to': rec.get_fiscal_manager_user().email,
                'subject': f"{rec.env.company.name} Contrôle: (Ref {rec.name or 'n/a'})",
                'body_html': email_body,
            }
            if rec.get_emails_for_department_head():
                mail_vals['email_cc'] = rec.get_emails_for_department_head()

            mail_id = self.env['mail.mail'].create(mail_vals)
            mail_id.send()

            template_id = rec.env.ref('bvortex_controls.email_template_document').id
            rec.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

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
            if not rec.action_ids:
                raise exceptions.UserError(
                    _("There are no actions on the form !!"))

            if not rec.user_ids:
                raise exceptions.UserError(
                    _("There are no users on the form !!"))

            if len(rec.action_ids) != len(rec.user_ids):
                raise exceptions.UserError(
                    _("The number of actions is different from the number of users !!"))

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
                    'category': rec.category,
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
            rec.out_of_time = False
            rec.on_time = False
            rec.state = 'cancel'

    def action_done(self):
        for rec in self:
            rec.out_of_time = False
            rec.on_time = False
            rec.state = 'done'
            message = _(f'Concluded Document !!')
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

    def action_draft(self):
        for rec in self:
            rec.out_of_time = False
            rec.on_time = False
            rec.state = 'draft'