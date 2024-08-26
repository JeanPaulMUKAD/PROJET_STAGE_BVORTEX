from odoo import api, fields, models, exceptions,_

class control_planingue_report(models.Model):
    _name = 'control.planingue.report'

    client = fields.Many2one('res.partner')
    nbr_jour = fields.Integer('nombre de jours')
    planingue_taches_ids = fields.One2many('control.planingue.taches','action_report_id','ligne des actions')
    planingue_id = fields.Many2one('control.planingue')
    etape = fields.Many2many('project.task.type')

    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ], string='Status', required=True,  copy=False,
        tracking=True, default='draft')

    type_selct = fields.Selection([
        ('ONEM', 'ONEM '),
        ('INPP', 'INPP '),
        ('CNSS', 'CNSS '),
        ('MINECO', 'MINECO '),

    ], string='Type select')


