from odoo import models, fields, api
from datetime import date, timedelta


class DeclarationTVA(models.Model):
    _name = "declaration_tva"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(string="Reference")
    last_declaration = fields.Many2one('declaration_tva', "Déclaration précédente")

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

    total_vat_collected = fields.Integer(string="Total de la TVA collectée")
    total_deductible_vat = fields.Integer(string="Total de la TVA déductible")
    vat_payable = fields.Integer(string="TVA Payable")
    vat_credit = fields.Integer(string="Crédit TVA")



    collaborator = fields.Many2one('res.users', string="Collaborateur")
    manager = fields.Many2one('res.users', string="Manager", required=True)
    partner_id = fields.Many2one('res.partner', string="Société", required=True)

    state = fields.Selection([('draft', 'Brouillon'), ('confirm', 'Confirmé'), ('validate', 'validé'), ('declared', 'Déclaré'), ('appured', 'Appuré'), ('delivered', 'Remis')], default="draft", string='Status')
    status = fields.Selection([('credit', 'Crédit'), ('payable', 'Payable')])

    sales_invoices = fields.Many2many('account.move', 'campaign_id', string="Facture clients")
    purchases_invoices = fields.Many2many('account.move', string="Facture Fourniseurs")

    releve_doc = fields.Binary(string='Relevé', attachment=True, help='Document de relevé')

    customer_total_amount_tcc_usd = fields.Float(string="Total des factures des clients en USD", default=0)
    customer_total_amount_tcc_cdf = fields.Float(string="Total des factures des clients en CDF", default=0)
    customer_total_amount_ht_usd = fields.Float(string="Total hors taxe des factures des clients en USD",default=0)
    customer_total_amount_ht_cdf = fields.Float(string="Total hors taxe des factures des clients en CDF",default=0)
    customer_vat_usd = fields.Float(string="TVA des factures des clients en USD", default=0)
    customer_vat_cdf = fields.Float(string="TVA des factures des clients en CDF", default=0)

    partner_total_amount_tcc_usd = fields.Float(string="Total des factures des fourniseurs en USD", default=0)
    partner_total_amount_tcc_cdf = fields.Float(string="Total des factures des fourniseurs en CDF", default=0)
    partner_total_amount_ht_usd = fields.Float(string="Total hors taxe des factures des fourniseurs en USD", default=0)
    partner_total_amount_ht_cdf = fields.Float(string="Total hors taxe des factures des fourniseurs en CDF", default=0)
    partner_vat_usd = fields.Float(string="TVA des factures des fourniseurs en USD", default=0)
    partner_vat_cdf = fields.Float(string="TVA des factures des fourniseurs en CDF", default=0)



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
        if self.mois:
            year = date.today().year
            month = self._get_month_number(self.mois)
            next_month = month + 1
            next_year = year
            if next_month > 12:
                next_month = 1
                next_year += 1
            return date(next_year, next_month, 15) - timedelta(days=1)
        else:
            return False

    @api.onchange('partner_id', 'mois')
    def _onchange_partner_id_mois(self):
        if self.partner_id and self.mois:
            start_date = self.start_date
            end_date = self.end_date
            sales_invoices = self.env['account.move'].search([
                ('partner_id', '=', self.partner_id.id),
                ('invoice_date', '>=', start_date),
                ('move_type', '=', 'out_invoice'),
                ('payment_state', 'in', ['posted', 'paid', 'partial']),
                ('invoice_date', '<=', end_date),
            ])
            self.sales_invoices = [(6, 0, sales_invoices.ids)]
            purchases_invoices = self.env['account.move'].search([
                ('partner_id', '=', self.partner_id.id),
                ('invoice_date', '>=', start_date),
                ('move_type', '=', 'in_invoice'),
                ('payment_state', 'in', ['posted', 'paid', 'partial']),
                ('invoice_date', '<=', end_date),
            ])
            self.purchases_invoices = [(6, 0, purchases_invoices.ids)]




    def save(self):
        pass

    def button_edit(self):
        pass

    def button_cancel(self):
        pass

    @api.onchange('sales_invoices', 'purchases_invoices', 'last_declaration')
    def _onchange_invoices(self):
        total_vat_collected = sum(invoice.amount_tax_signed for invoice in self.sales_invoices)

        total_deductible_vat = sum(invoice.amount_tax_signed for invoice in self.purchases_invoices)

        vat_credit = 0

        declaration_tva = self.last_declaration

        if declaration_tva.vat_credit == 0 :
            vat_payable = total_vat_collected + total_deductible_vat
            if vat_payable < 0 :
                vat_credit = vat_payable
                vat_payable = 0
        else :
            vat_credit = self.last_declaration.vat_credit
            vat_payable = total_vat_collected + total_deductible_vat + vat_credit
            vat_credit = vat_payable
            vat_payable = 0
            if vat_credit >= 0:
                vat_payable = vat_credit
                vat_credit = 0


        self.write({
            'total_vat_collected': total_vat_collected,
            'total_deductible_vat': total_deductible_vat,
            'vat_credit': vat_credit,
            'vat_payable': vat_payable,
        })

    @api.model
    def get_customer_invoices(self):
        customer_invoices = []
        for invoice in self.sales_invoices:
            customer_name = invoice.partner_id.name
            invoice_info = {
                'partner': customer_name,
                'tax_number': invoice.partner_id.vat,
                'designation': invoice.partner_id.commercial_company_name,
                'date': invoice.invoice_date,
                'invoice_reference': invoice.name,
                'montant_ttc_usd' : invoice.amount_tax_signed,
                'montant_ttc_cdf' : invoice.amount_tax_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,
                'montant_ht_usd' : invoice.amount_untaxed_signed,
                'montant_ht_cdf' : invoice.amount_untaxed_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,
                'vat_usd' : invoice.amount_tax_signed,
                'vat_cdf' : invoice.amount_tax_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,

            }
            customer_invoices.append(invoice_info)

            self.customer_total_amount_tcc_usd += invoice_info['montant_ttc_usd']
            self.customer_total_amount_tcc_cdf += invoice_info['montant_ttc_cdf']
            self.customer_total_amount_ht_usd += invoice_info['montant_ht_usd']
            self.customer_total_amount_ht_cdf += invoice_info['montant_ht_cdf']
            self.customer_vat_usd += invoice_info['vat_usd']
            self.customer_vat_cdf += invoice_info['vat_cdf']

        return customer_invoices

    @api.model
    def get_partner_invoices(self):
        customer_invoices = []
        for invoice in self.purchases_invoices:
            customer_name = invoice.partner_id.name
            invoice_info = {
                'partner': customer_name,
                'tax_number': invoice.partner_id.vat,
                'designation': invoice.partner_id.commercial_company_name,
                'date': invoice.invoice_date,
                'invoice_reference': invoice.name,
                'montant_ttc_usd' : invoice.amount_tax_signed,
                'montant_ttc_cdf' : invoice.amount_tax_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,
                'montant_ht_usd' : invoice.amount_untaxed_signed,
                'montant_ht_cdf' : invoice.amount_untaxed_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,
                'vat_usd' : invoice.amount_tax_signed,
                'vat_cdf' : invoice.amount_tax_signed * self.get_active_currency_rate() if self.get_active_currency_rate() != None else 1,

            }
            customer_invoices.append(invoice_info)

            self.partner_total_amount_tcc_usd += invoice_info['montant_ttc_usd']
            self.partner_total_amount_tcc_cdf += invoice_info['montant_ttc_cdf']
            self.partner_total_amount_ht_usd += invoice_info['montant_ht_usd']
            self.partner_total_amount_ht_cdf += invoice_info['montant_ht_cdf']
            self.partner_vat_usd += invoice_info['vat_usd']
            self.partner_vat_cdf += invoice_info['vat_cdf']

        return customer_invoices


    @api.model
    def get_active_currency_rate(self):
        active_currencies = self.env['res.currency'].search([('active', '=', True)])
        cdf_currency = active_currencies.filtered(lambda c: c.name == 'CDF')
        if cdf_currency:
            return cdf_currency.rate_ids.company_rate
        else:
            return None
