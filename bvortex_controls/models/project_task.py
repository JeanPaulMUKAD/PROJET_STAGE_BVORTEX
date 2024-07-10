
from odoo import api, Command, fields, models, tools, SUPERUSER_ID, _, _lt
from odoo.exceptions import UserError, ValidationError, AccessError

class project_task(models.Model):
    _inherit = "project.task"

    document_id = fields.Many2one('control.document', string="Document")
    category = fields.Selection(selection=[
        ('spontanne', 'Contrôle Spontanné'),
        ('fiscal', 'Contrôle Fiscal'),
        ('parafiscal', 'Parafiscalité'),
    ], string='Category', required=True, default='spontanne')