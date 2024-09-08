from odoo import api, fields, models, exceptions,_

class control_planingue_report(models.Model):
    _name = 'control.planingue.free.line'

    client = fields.Many2one('res.partner')
    date_debut = fields.Date('Date Debut')
    date_fin = fields.Date('Date Fin')
    planingue_id = fields.Many2one('control.planingue')
    etape = fields.Many2many('project.task.type')
    planingue_taches_ids = fields.One2many('control.planingue.taches','action_free','ligne des actions')


    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False,
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

    @api.onchange('date_debut', 'date_fin', 'planingue_id')
    def _onchange_dates(self):
        if self.planingue_id:
            planingue = self.planingue_id
            if planingue.date_debut and planingue.date_fin:
                if self.date_debut and self.date_fin:
                    if (
                            self.date_debut < planingue.date_debut or self.date_debut > planingue.date_fin or self.date_fin < planingue.date_debut or self.date_fin > planingue.date_fin):
                        raise exceptions.UserError(_("Les dates ne sont pas dans l'intervalle des dates du planingue."))



