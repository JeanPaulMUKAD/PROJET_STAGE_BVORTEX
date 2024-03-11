from odoo import models, fields, api
from datetime import date, timedelta, datetime




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
    annee = fields.Integer(string="Année", compute="_compute_year", store=True)



    total_vat_collected = fields.Float(string="Total de la TVA collectée")
    total_vat_collected_cdf = fields.Float(string="Total de la TVA collectée en Fc")

    total_deductible_vat = fields.Float(string="Total de la TVA déductible")
    total_deductible_vat_cdf= fields.Float(string="Total de la TVA déductible en FC")

    vat_payable = fields.Float(string="TVA Payable")
    vat_payable_cdf = fields.Float(string="TVA Payable En Fc")

    vat_credit = fields.Float(string="Crédit TVA")
    vat_credit_cdf = fields.Float(string="Crédit TVA en Fc")



    collaborator = fields.Many2one('res.users', string="Collaborateur")
    manager = fields.Many2one('res.users', string="Manager", required=True)
    partner_id = fields.Many2one('res.partner', string="partenaire")
    company_id = fields.Many2one('res.company', string="Société", required=True)

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

    month_exchange_rates = fields.Float("Taux de change de la déclaration", store=True, default=1)

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
    def _compute_month_rate(self):
        self.month_exchange_rates = self.get_active_currency_rate()

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

    @api.depends('mois')
    def _compute_year(self):
        for declaration in self:
            if declaration.mois:
                current_year = fields.Date.today().year
                declaration.annee = current_year
            else:
                declaration.annee = False

    @api.onchange('company_id', 'mois')
    def _onchange_partner_id_mois(self):
        if self.company_id and self.mois:
            start_date = self.start_date
            end_date = self.end_date
            sales_invoices = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
                ('invoice_date', '>=', start_date),
                ('move_type', '=', 'out_invoice'),
                ('payment_state', 'in', ['posted', 'paid', 'partial']),
                ('invoice_date', '<=', end_date),
            ])
            self.sales_invoices = [(6, 0, sales_invoices.ids)]
            purchases_invoices = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
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

        if declaration_tva:
            vat_payable = total_vat_collected + total_deductible_vat + declaration_tva.vat_credit
            if vat_payable < 0:
                vat_credit = vat_payable
                vat_payable = 0
            else :
                vat_credit = 0
            self.vat_credit = vat_credit
            self.vat_credit_cdf = vat_credit * self.month_exchange_rates
        else:
            vat_payable = total_vat_collected + total_deductible_vat
            if vat_payable < 0:
                vat_credit = vat_payable
                vat_payable = 0
            else:
                vat_credit = 0
            self.vat_credit = 0
            self.vat_credit_cdf = 0


        self.write({
            'total_vat_collected': total_vat_collected,
            'total_deductible_vat': total_deductible_vat,
            'vat_credit': vat_credit,
            'vat_payable': vat_payable,
            'vat_payable_cdf' : vat_payable * self.month_exchange_rates
        })


    @api.model
    def get_customer_invoices(self):
        customer_invoices = []
        s_total_amount_tcc_usd = 0
        s_total_amount_tcc_cdf = 0
        s_total_amount_ht_usd = 0
        s_total_amount_ht_cdf = 0
        s_vat_usd = 0
        s_vat_cdf = 0


        for invoice in self.sales_invoices:
            s_total_amount_tcc_usd += invoice.amount_tax_signed
            s_total_amount_tcc_cdf += invoice.amount_tax_signed * self.month_exchange_rates
            s_total_amount_ht_usd += invoice.amount_untaxed_signed
            s_total_amount_ht_cdf += invoice.amount_untaxed_signed * self.month_exchange_rates
            s_vat_usd += invoice.amount_tax_signed
            s_vat_cdf += invoice.amount_tax_signed * self.month_exchange_rates

            invoice_info = {
                'partner': invoice.partner_id.name,
                'tax_number': invoice.partner_id.vat,
                'designation': invoice.partner_id.commercial_company_name,
                'date': invoice.invoice_date,
                'invoice_reference': invoice.name,
                'montant_ttc_usd' : invoice.amount_tax_signed,
                'montant_ttc_cdf' : invoice.amount_tax_signed * self.month_exchange_rates,
                'montant_ht_usd' : invoice.amount_untaxed_signed,
                'montant_ht_cdf' : invoice.amount_untaxed_signed * self.month_exchange_rates,
                'vat_usd' : invoice.amount_tax_signed,
                'vat_cdf' : invoice.amount_tax_signed * self.month_exchange_rates,

            }
            customer_invoices.append(invoice_info)

        self.customer_total_amount_tcc_usd = s_total_amount_tcc_usd
        self.customer_total_amount_tcc_cdf = s_total_amount_tcc_cdf
        self.customer_total_amount_ht_usd = s_total_amount_ht_usd
        self.customer_total_amount_ht_cdf = s_total_amount_ht_cdf
        self.customer_vat_usd = s_vat_usd
        self.customer_vat_cdf = s_vat_cdf

        self.total_vat_collected = s_vat_usd
        self.total_vat_collected_cdf = s_vat_cdf

        return customer_invoices

    @api.model
    def get_partner_invoices(self):
        customer_invoices = []
        s_total_amount_tcc_usd = 0
        s_total_amount_tcc_cdf = 0
        s_total_amount_ht_usd = 0
        s_total_amount_ht_cdf = 0
        s_vat_usd = 0
        s_vat_cdf = 0
        for invoice in self.purchases_invoices:
            s_total_amount_tcc_usd += invoice.amount_tax_signed
            s_total_amount_tcc_cdf += invoice.amount_tax_signed * self.month_exchange_rates
            s_total_amount_ht_usd += invoice.amount_untaxed_signed
            s_total_amount_ht_cdf += invoice.amount_untaxed_signed * self.month_exchange_rates
            s_vat_usd += invoice.amount_tax_signed
            s_vat_cdf += invoice.amount_tax_signed * self.month_exchange_rates

            invoice_info = {
                'partner': invoice.partner_id.name,
                'tax_number': invoice.partner_id.vat,
                'designation': invoice.partner_id.commercial_company_name,
                'date': invoice.invoice_date,
                'invoice_reference': invoice.name,
                'montant_ttc_usd' : invoice.amount_tax_signed,
                'montant_ttc_cdf' : invoice.amount_tax_signed * self.month_exchange_rates,
                'montant_ht_usd' : invoice.amount_untaxed_signed,
                'montant_ht_cdf' : invoice.amount_untaxed_signed * self.month_exchange_rates,
                'vat_usd' : invoice.amount_tax_signed,
                'vat_cdf' : invoice.amount_tax_signed * self.month_exchange_rates,

            }
            customer_invoices.append(invoice_info)

            self.partner_total_amount_tcc_usd = s_total_amount_tcc_usd
            self.partner_total_amount_tcc_cdf = s_total_amount_tcc_cdf
            self.partner_total_amount_ht_usd = s_total_amount_ht_usd
            self.partner_total_amount_ht_cdf = s_total_amount_ht_cdf
            self.partner_vat_usd = s_vat_usd
            self.partner_vat_cdf = s_vat_cdf

            self.total_deductible_vat = s_vat_usd
            self.total_deductible_vat_cdf = s_vat_cdf


        return customer_invoices


    @api.model
    def compute_tva_values(self):
        result = []

        declarations = self.env['declaration_tva'].search([('company_id', '=', self.company_id.id), ('annee', '=', self.annee)])

        for declaration in declarations:
            declaration_month = declaration.mois

            realized_sales = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
                ('move_type', '=', 'out_invoice'),
                ('invoice_month', '=', declaration_month)
            ])
            total_ca_usd = 0
            total_taxable_ca_usd = 0

            for invoice in self.sales_invoices:
                total_taxable_ca_usd += invoice.amount_tax_signed

            for invoice in realized_sales:
                total_ca_usd += invoice.amount_tax_signed

            declaration_info = {
                'mois': declaration.mois,
                'exchange_rate' : declaration.month_exchange_rates,
                'vat_deductible_usd': declaration.total_deductible_vat,
                'vat_deductible_cdf': declaration.total_deductible_vat_cdf,
                'realized_ca_usd': total_ca_usd,
                'realized_ca_cdf': total_ca_usd * self.month_exchange_rates,
                'taxable_ca_usd': total_taxable_ca_usd,
                'taxable_ca_cdf': total_taxable_ca_usd * self.month_exchange_rates,
                'collected_vat_usd': self.total_vat_collected,
                'collected_vat_cdf' : self.total_vat_collected_cdf,
                'net_vat_usd': self.vat_payable,
                'net_vat_cdf': self.vat_payable * self.month_exchange_rates,
            }

            result.append(declaration_info)





class AcountMove(models.Model):
    _inherit = 'account.move'
    invoice_month = fields.Char("Mois de la facture", compute="_compute_month")

    @api.depends('invoice_date')
    def _compute_month(self):
        month = self.invoice_date.strftime('%B')
        return month