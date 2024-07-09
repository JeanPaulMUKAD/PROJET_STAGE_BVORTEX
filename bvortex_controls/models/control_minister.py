from odoo import api, fields, models, _

class control_minister(models.Model):
    _name = 'control.minister'

    code = fields.Char('Code', readonly=True)
    name = fields.Char('Name')
    color = fields.Char('Color')
    deadline = fields.Integer('Deadline', default=5)
    tag_id = fields.Many2one('project.tags')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('control.minister') or 'MIN'
            msg_body = 'Control Minister Created'
            for msg in self:
                msg.message_post(body=msg_body)
            result = super(control_minister, self).create(vals_list)
            result.tag_id = self.env['project.tags'].create(
                {
                    'name': result.name,
                    'color': result.color
                }
            ).id
        return result