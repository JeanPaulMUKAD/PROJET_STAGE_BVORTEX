from odoo import api, fields, models, exceptions, _


class control_planingue_taches(models.Model):
    _name = 'control.planingue.taches'

    nom = fields.Char('Nom')
    utilisateur = fields.Many2many('res.users', 'utilisateur')
    date = fields.Date('Date')
    action_id = fields.Many2one('control.planingue.line')
    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')

    @api.onchange('date','action_id')
    def _onchange_dates2(self):
        if self.action_id:
            planingue = self.action_id
            if planingue.date_debut and planingue.date_fin:
                if self.date:
                    if (self.date < planingue.date_debut or self.date > planingue.date_fin):
                        raise exceptions.UserError(_("La date n'est pas dans l'intervalle des dates du planingue."))



