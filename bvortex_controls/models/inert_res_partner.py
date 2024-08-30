from odoo import api, Command, fields, models, tools, SUPERUSER_ID, _, _lt
class innert_res(models.Model):
    _inherit = "res.partner"


    project_count = fields.Integer(compute='project_compute_count')
    project_ids = fields.One2many('project.project')



    def get_project(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'project',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.project',
            'domain': [('id', '=', self.project_ids.ids)],
            'context': {
                'create': True,
                'search_default_partner_id': self.id,
                'default_partner_id': self.id,
            }
        }

    def project_compute_count(self):
        for record in self:
            record.project_count = self.env['project.project'].search_count([('partner_id', '=', self.id)])
