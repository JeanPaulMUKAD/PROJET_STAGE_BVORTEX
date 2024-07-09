from odoo import api, fields, models, _

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
    task_ids = fields.Many2many('project.task', string="Tasks")
    action_ids = fields.Many2many('control.action', string="Actions")
    user_ids = fields.Many2many('res.users', string="Assignees")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')

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
            rec.state = 'confirmed'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'