from odoo import models, fields, api
from datetime import date, timedelta


class DeclarationTVA(models.Model):
    _name = "declaration_tva"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(string="Reference")

    mois = fields.Selection([
        ('janvier', 'Janvier'),
        ('février', 'Février'),
        ('mars', 'Mars'),
        ('avril', 'Avril'),
        ('mai', 'Mai'),
        ('juin', 'Juin'),
        ('juillet', 'Juillet'),
        ('août', 'Août'),
        ('septembre', 'Septembre'),
        ('octobre', 'Octobre'),
        ('novembre', 'Novembre'),
        ('décembre', 'Décembre'),
    ], string='Mois', required=True)

    start_date = fields.Date(string="Date de début", default=lambda self: self._get_default_start_date(), compute="_compute_dates", required=True)
    end_date = fields.Date(string="Date de fin", default=lambda self: self._get_default_end_date(), compute="_compute_dates", required=True)
    total_purchases = fields.Integer(string="Total des achats")
    total_sales = fields.Integer(string="Total des achats")
    collaborator = fields.Many2one('res.users', string="Collaborateur")
    manager = fields.Many2one('res.users', string="Manager", required=True)

    partner_id = fields.Many2one('res.partner', string="Société", required=True)
    state = fields.Selection([('draft', 'Brouillon'), ('confirm', 'Confirmé'), ('validate', 'validé'), ('declared', 'Déclaré'), ('appured', 'Appuré'), ('cancel', 'Annulé')], default="draft", string='Status')
    sales_invoices = fields.Many2many('account.move', 'campaign_id', string="Facture clients")
    purchases_invoices = fields.Many2many('account.move', string="Facture Fourniseurs")



    @api.depends('mois')
    def _compute_dates(self):
        for record in self:
            if record.mois:
                year = date.today().year
                month = self._get_month_number(record.mois)
                record.start_date = date(year, month, 15)
                next_month = month + 1
                next_year = year
                if next_month > 12:
                    next_month = 1
                    next_year += 1
                record.end_date = date(next_year, next_month, 15)
            else:
                record.start_date = False
                record.end_date = False

    def _get_month_number(self, month_name):
        months = {
            'janvier': 1,
            'février': 2,
            'mars': 3,
            'avril': 4,
            'mai': 5,
            'juin': 6,
            'juillet': 7,
            'août': 8,
            'septembre': 9,
            'octobre': 10,
            'novembre': 11,
            'décembre': 12,
        }
        return months.get(month_name)

    @api.model
    def _get_default_start_date(self):
        if self.mois:
            year = date.today().year
            month = self._get_month_number(self.mois)
            return date(year, month, 15)

    @api.model
    def _get_default_end_date(self):
        if self.start_date:
            return self.start_date + timedelta(days=30)

    def save(self):
        pass

    def button_edit(self):
        pass

    def button_cancel(self):
        pass


