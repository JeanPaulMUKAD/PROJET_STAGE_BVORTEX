from odoo import api, Command, fields,exceptions,models, tools, SUPERUSER_ID, _, _lt
from odoo.exceptions import UserError, ValidationError, AccessError


class project_task(models.Model):
    _inherit = "project.task"

    document_id = fields.Many2one('control.document', string="Document")
    action_id = fields.Many2one('control.action', string="Action")
    category = fields.Selection(string='Category', related='document_id.category')
    task_task = fields.Many2one('control.planingue.taches', string="tache dans action")
    statut_ch = fields.Many2one('control.planingue.line', string="statut")
    planingue = fields.Many2one('control.planingue' ,string="planingue")


    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        ch = "draft"
        if self.stage_id.name == 'DRAFT':
            ch = "draft"
        if self.stage_id.name == 'ÉTABLIE':
            ch = "etablie"
        if self.stage_id.name == 'REVUE':
            ch = "revue"
        if self.stage_id.name == 'VALIDER':
            ch = "valider"
        if self.stage_id.name == 'PAYER':
            ch = "payer"
        if self.stage_id.name == 'DECLARER':
            ch = "déclarer"
        if self.stage_id.name == 'APURER':
            ch = "apurer"
        if self.stage_id.name == 'ARCHIVER':
            ch = "archiver"
        if self.stage_id.name == 'TRANSMIS':
            ch = "transmis"

        self.statut_ch.statut = ch

        if self.stage_id.name != 'DRAFT':
            if self.stage_id.name != 'TRANSMIS':
               self.task_task.statut = 'in_progress'
            else:
                self.task_task.statut = 'done'
        else:
            self.task_task.statut = 'draft'

    def action_cancelled(self):
        for task in self:
            task.stage_id = self.env.ref('bvortex_controls.cancelled_stage').id

    def action_concluded(self):
        for task in self:
            task.stage_id = self.env.ref('bvortex_controls.concluded_stage').id
