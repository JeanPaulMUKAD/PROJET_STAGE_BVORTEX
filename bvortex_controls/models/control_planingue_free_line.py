from odoo import api, fields, models, exceptions,_

class control_planingue_report(models.Model):
    _name = 'control.planingue.free.line'

    client = fields.Many2one('res.partner')
    date_debut = fields.Date('Date Debut')
    date_fin = fields.Date('Date Fin')
    planingue_id = fields.Many2one('control.planingue')
    etape = fields.Many2many('project.task.type')

    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
    ], string='Status', required=True,  copy=False,
        tracking=True, default='draft')

    type_selct = fields.Selection([
        ('ONEM', 'ONEM'),
        ('INPP', 'INPP'),
        ('CNSS', 'CNSS'),
        ('MINECO', 'MINECO'),
        ('INDUSTRIE', 'INDUSTRIE'),
        ('IPR', 'IPR'),
        ('TVA', 'TVA'),

    ], string='Type select')


