from odoo import api, fields, models, exceptions,_

class control_planingue_line(models.Model):
    _name = 'control.planingue.line'

    client = fields.Many2one('res.partner')
    date_debut = fields.Date('Date Debut')
    date_fin = fields.Date('Date Fin')
    planingue_taches_ids = fields.One2many('control.planingue.taches','action_id','ligne des actions')
    planingue_id = fields.Many2one('control.planingue')
    project_ids = fields.One2many('project.project','planingue_line_id')

    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Status', required=True,  copy=False,
        tracking=True, default='draft')

    type_selct = fields.Selection([
        ('ONEM', 'ONEM '),
        ('INPP', 'INPP '),
        ('CNSS', 'CNSS '),
        ('MINECO', 'MINECO '),
        ('INDUSTRIE', 'INDUSTRIE '),
        ('IPR', 'IPR '),
        ('TVA', 'TVA'),

    ], string='Type select')

    @api.onchange('date_debut', 'date_fin', 'planingue_id')
    def _onchange_dates(self):
        if self.planingue_id:
            planingue = self.planingue_id
            if planingue.date_debut and planingue.date_fin:
                if self.date_debut and self.date_fin:
                    if (self.date_debut < planingue.date_debut or self.date_debut > planingue.date_fin or self.date_fin < planingue.date_debut or self.date_fin > planingue.date_fin):
                        raise exceptions.UserError(_("Les dates ne sont pas dans l'intervalle des dates du planingue."))

   

