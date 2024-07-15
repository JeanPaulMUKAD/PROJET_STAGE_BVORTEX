from odoo import api, fields, models, _


class control_nature(models.Model):
    _name = 'control.nature'

    code = fields.Char('Code', readonly=True)
    name = fields.Char('Name')
    color = fields.Char('Color')
    tag_id = fields.Many2one('project.tags')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('control.nature') or 'NAT'
            msg_body = 'Control Nature Created'
            for msg in self:
                msg.message_post(body=msg_body)
            result = super(control_nature, self).create(vals_list)
            result.tag_id = self.env['project.tags'].create(
                {
                    'name': result.name,
                    'color': result.color
                }
            ).id
        return result

    def write(self, vals):
        res = super(control_nature, self).write(vals)
        if 'name' in vals:
            for record in self:
                if record.tag_id:
                    record.tag_id.name = record.name
        return res

    def unlink(self):
        for record in self:
            if record.tag_id:
                record.tag_id.unlink()
        return super(control_nature, self).unlink()
