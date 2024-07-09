from odoo import api, fields, models, _

class control_action(models.Model):
    _name = 'control.action'

    name = fields.Char('Name')
    code = fields.Char('Code', readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('control.action') or 'ACT'
            msg_body = 'Control Action Created'
            for msg in self:
                msg.message_post(body=msg_body)
            result = super(control_action, self).create(vals_list)
        return result