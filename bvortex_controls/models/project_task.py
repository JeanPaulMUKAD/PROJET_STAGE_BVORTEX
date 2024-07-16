from odoo import api, Command, fields, models, tools, SUPERUSER_ID, _, _lt
from odoo.exceptions import UserError, ValidationError, AccessError


class project_task(models.Model):
    _inherit = "project.task"

    document_id = fields.Many2one('control.document', string="Document")
    action_id = fields.Many2one('control.action', string="Action")
    category = fields.Selection(string='Category', related='document_id.category')

    def action_cancelled(self):
        for task in self:
            task.stage_id = self.env.ref('bvortex_controls.cancelled_stage').id

    def action_concluded(self):
        for task in self:
            task.stage_id = self.env.ref('bvortex_controls.concluded_stage').id
