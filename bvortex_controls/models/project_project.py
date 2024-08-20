
from odoo import api, Command, fields, models, tools, SUPERUSER_ID, _, _lt
class Project(models.Model):
    _inherit = "project.project"

    is_fiscal_project = fields.Boolean(String="Is this a Fiscale project ?", default=False)
    planingue_id = fields.Many2many('control.planingue')
    planingue_line_id = fields.Many2one('control.planingue.line')

