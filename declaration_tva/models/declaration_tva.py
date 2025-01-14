from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date, timedelta
import random


class DeclarationTVA(models.Model):
    _name = "declaration_tva"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(string="Reference", tracking=True)
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
    partner_id = fields.Many2one('res.partner', string="Partenaire")
    company_id = fields.Many2one('res.company', string="Société", required=True)

    state = fields.Selection([('draft', 'Brouillon'), ('confirm', 'Envoyé'), ('validate', 'validé'), ('declared', 'Déclaré'), ('appured', 'Appuré'), ('delivered', 'Remis')], default="draft", string='Status')
    status = fields.Selection([('credit', 'Crédit'), ('payable', 'Payable')])

    sales_invoices = fields.Many2many('account.move', 'campaign_id', string="Facture clients")
    purchases_invoices = fields.Many2many('account.move', 'name', string="Facture Fourniseurs")
    realize_ca = fields.Many2many('account.move', 'activity_ids', string="Chiffre d'affaire réalisé")



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

    month_exchange_rates = fields.Float("Taux de change de la déclaration", store=True, default=1,  tracking=True)

    liquidation_statement = fields.Many2many("bulletin_liquidation", requiered=True)
    
    total_bulletin_ht_usd = fields.Float(string="Total Hors tax des bulletins de liquidation en USD", default=0)
    total_bulletin_ht_cdf = fields.Float(string="Total Hors tax des bulletins de liquidation en CDF", default=0)
    total_vat_bulletin_usd = fields.Float(string="Total de la TVA des bulletins de liquidation en USD", default=0)
    total_vat_bulletin_cdf = fields.Float(string="Total de la TVA des bulletins de liquidation en CDF", default=0)


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
                ('payment_state', 'in', ['posted', 'paid', 'partial', 'in_payment']),
                ('invoice_date', '<=', end_date),
            ])
            self.sales_invoices = [(6, 0, sales_invoices.ids)]

            purchases_invoices = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
                ('invoice_date', '>=', start_date),
                ('move_type', '=', 'in_invoice'),
                ('payment_state', 'in', ['posted', 'paid', 'partial', 'in_payment']),
                ('invoice_date', '<=', end_date),
            ])
            self.purchases_invoices = [(6, 0, purchases_invoices.ids)]

            realize_ca = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
                ('move_type', '=', 'out_invoice'),
                ('invoice_month', '=', self.mois)
            ])
            self.realize_ca = [(6, 0, realize_ca.ids)]

            bulletin_liquidation = self.env['bulletin_liquidation'].search([
                ('company_id', '=', self.company_id.id),
                ('date', '>=', start_date),
                ('state', '=', 'done'),
                ('date', '<=', end_date),
            ])
            self.liquidation_statement = [(6, 0, bulletin_liquidation.ids)]

    def button_confirm(self):
        self.write({'state': 'confirm'})
        self.generate_reference()



        manager_user = self.manager
        declaration_view_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url') + \
                               '/web#id=%s&view_type=form&model=declaration_tva' % self.id

        notification = self.env['mail.activity'].create({
            'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
            'note': 'Nouvelle déclaration TVA à valider. Cliquez <a href="%s">ici</a> pour voir la déclaration.' % declaration_view_url,
            'res_id': self.id,
            'user_id': manager_user.id,
            'date_deadline': fields.Date.today(),
            'summary': 'Validation de déclaration TVA',
            'res_model_id': self.env.ref('declaration_tva.model_declaration_tva').id,
        })

        return True



    def button_edit(self):
        self.write({'state': 'draft'})


    def button_validate(self):
        self.write({'state': 'validate'})

    def button_declare(self):
        # Mettre à jour l'état de la déclaration
        self.write({'state': 'declared'})
        self.write_invoice_state()

        for declaration in self:
            # Obtenir le journal par défaut pour les déclarations de TVA
            default_journal = self.env['account.journal'].search([('type', '=', 'general')], limit=1)

            # Obtenir les comptes TVA configurés dans la société
            total_collected_vat_account = declaration.company_id.total_collected_vat_account
            total_deductible_vat_account = declaration.company_id.total_deductible_vat_account
            credit_vat_account = declaration.company_id.credit_vat_account
            vat_payable_account = declaration.company_id.vat_payable_account
            company_nature = declaration.company_id.company_nature


            if not total_collected_vat_account or not total_collected_vat_account or not total_deductible_vat_account or not credit_vat_account:
                raise UserError("Aucun compte de de TVA configuré ! Pensez à en configurer au niveau des paramètres ou contactez l'administrateur.")
            elif not  company_nature :
                raise UserError("Le champs type de la société n'est pas configuré, pensez à le faire.")


            # Vérifier si la TVA est créditrice ou payable
            if declaration.vat_credit > 0:
                # Passer les écritures pour le crédit de TVA
                move_vals = {
                    'journal_id': default_journal.id,
                    'date': fields.Date.today(),
                    'ref': 'Ecriture pour crédit de TVA',
                    'line_ids': [
                        (0, 0, {
                            'account_id': total_deductible_vat_account.id,
                            'name': 'TVA déductible',
                            'debit': 0.0,
                            'credit': declaration.vat_credit,
                        }),
                        (0, 0, {
                            'account_id': credit_vat_account.id,
                            'name': 'Crédit TVA',
                            'debit': declaration.vat_credit,
                            'credit': 0.0,
                        }),
                    ],
                }
            else:
                # Passer les écritures pour la TVA payable
                move_vals = {
                    'journal_id': default_journal.id,
                    'date': fields.Date.today(),
                    'ref': 'Ecriture pour TVA payable',
                    'line_ids': [
                        (0, 0, {
                            'account_id': total_collected_vat_account.id,
                            'name': 'TVA collectée',
                            'debit': declaration.vat_payable,
                            'credit': 0.0,
                        }),
                        (0, 0, {
                            'account_id': vat_payable_account.id,
                            'name': 'TVA payable',
                            'debit': 0.0,
                            'credit': declaration.vat_payable,
                        }),
                    ],
                }

            # Créer l'écriture comptable
            move_id = self.env['account.move'].create(move_vals)

            # Valider l'écriture comptable
            move_id.action_post()

    def button_approve(self):
        self.write({'state': 'appured'})


    def button_deliver(self):
        self.write({'state': 'delivered'})

    def save(self):
        self.generate_reference()

    def generate_reference(self):
        if not self.reference:
            declaration_year = self.annee
            declaration_month = self.mois
            company = self.company_id.name
            number = random.randint(1, 1_000_000)
            reference = f"DEC/{declaration_year}/{declaration_month}/{company}/{number}"
            self.write({'reference': reference})
        else :
            self.write({'reference': self.reference})


    @api.onchange('sales_invoices', 'purchases_invoices', 'last_declaration', 'liquidation_statement')
    def _onchange_invoices(self):
        total_vat_collected = sum(invoice.amount_tax_signed for invoice in self.sales_invoices)
        total_deductible_vat = sum(invoice.amount_tax_signed for invoice in self.purchases_invoices)
        total_bulletin_liquidation = sum(bulletin.total_vat for bulletin in self.liquidation_statement)

        vat_credit = 0
        declaration_tva = self.last_declaration

        if declaration_tva:
            vat_payable = total_vat_collected + total_deductible_vat - total_bulletin_liquidation + declaration_tva.vat_credit
            if vat_payable < 0:
                vat_credit = vat_payable
                vat_payable = 0
            else :
                vat_credit = 0
            self.vat_credit = vat_credit
            self.vat_credit_cdf = vat_credit * self.month_exchange_rates
        else:
            vat_payable = total_vat_collected + total_deductible_vat - total_bulletin_liquidation
            if vat_payable < 0:
                vat_credit = vat_payable
                vat_payable = 0
            else:
                vat_credit = 0
            self.vat_credit = 0
            self.vat_credit_cdf = 0


        self.write({
            'total_vat_collected': total_vat_collected,
            'total_deductible_vat': total_deductible_vat - total_bulletin_liquidation ,
            'vat_credit': vat_credit,
            'vat_payable': vat_payable,
            'vat_payable_cdf' : vat_payable * self.month_exchange_rates,
            'total_bulletin_ht_usd': total_bulletin_liquidation,
            'total_bulletin_ht_cdf': total_bulletin_liquidation * self.month_exchange_rates,
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
            s_total_amount_tcc_usd += invoice.amount_total_signed
            s_total_amount_tcc_cdf += invoice.amount_total_signed * self.month_exchange_rates
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
                'montant_ttc_usd' : invoice.amount_total_signed,
                'montant_ttc_cdf' : invoice.amount_total_signed * self.month_exchange_rates,
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
        partner_invoices = []
        s_total_amount_tcc_usd = 0
        s_total_amount_tcc_cdf = 0
        s_total_amount_ht_usd = 0
        s_total_amount_ht_cdf = 0
        s_vat_usd = 0
        s_vat_cdf = 0
        for invoice in self.purchases_invoices:
            s_total_amount_tcc_usd += invoice.amount_total_signed
            s_total_amount_tcc_cdf += invoice.amount_total_signed * self.month_exchange_rates
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
                'montant_ttc_usd' : invoice.amount_total_signed,
                'montant_ttc_cdf' : invoice.amount_total_signed * self.month_exchange_rates,
                'montant_ht_usd' : invoice.amount_untaxed_signed,
                'montant_ht_cdf' : invoice.amount_untaxed_signed * self.month_exchange_rates,
                'vat_usd' : invoice.amount_tax_signed,
                'vat_cdf' : invoice.amount_tax_signed * self.month_exchange_rates,

            }

            partner_invoices.append(invoice_info)

        self.partner_total_amount_tcc_usd = s_total_amount_tcc_usd
        self.partner_total_amount_tcc_cdf = s_total_amount_tcc_cdf
        self.partner_total_amount_ht_usd = s_total_amount_ht_usd
        self.partner_total_amount_ht_cdf = s_total_amount_ht_cdf
        self.partner_vat_usd = s_vat_usd
        self.partner_vat_cdf = s_vat_cdf

        self.total_deductible_vat = s_vat_usd - self.total_vat_bulletin_usd
        self.total_deductible_vat_cdf = s_vat_cdf - self.total_vat_bulletin_cdf


        return partner_invoices




    @api.model
    def declaration_recap(self):
        result = []
        total = []

        declarations = self.env['declaration_tva'].search([('company_id', '=', self.company_id.id), ('annee', '=', self.annee)])
        total_deductible_vat_usd = 0
        total_deductible_vat_cdf = 0
        total_ca_realise_usd = 0
        total_ca_realise_cdf = 0
        total_ca_imposable_usd = 0
        total_ca_imposable_cdf = 0
        total_tva_collecte_usd = 0
        total_tva_collecte_cdf = 0
        total_tva_nette_usd = 0
        total_tva_nette_cdf = 0

        for declaration in declarations:

            total_ca_usd = 0
            total_taxable_ca_usd = 0


            for invoice in declaration.sales_invoices:
                total_taxable_ca_usd += invoice.amount_total_signed

            realized_invoices = self.env['account.move'].search([
                ('company_id', '=', self.company_id.id),
                ('invoice_date', '>=', declaration.start_date),
                ('move_type', '=', 'out_invoice'),
                ('invoice_date', '<=', declaration.end_date),
            ])

            for invoice in realized_invoices:
                total_ca_usd += invoice.amount_total_signed
            self.write({'realize_ca': realized_invoices})


            declaration_info = {
                'company_name' : self.company_id,
                'mois': declaration.mois,
                'exchange_rate' : declaration.month_exchange_rates,
                'vat_deductible_usd': declaration.total_deductible_vat,
                'vat_deductible_cdf': declaration.total_deductible_vat * declaration.month_exchange_rates,
                'realized_ca_usd': total_ca_usd,
                'realized_ca_cdf': total_ca_usd * declaration.month_exchange_rates,
                'taxable_ca_usd': total_taxable_ca_usd,
                'taxable_ca_cdf': total_taxable_ca_usd * declaration.month_exchange_rates,
                'collected_vat_usd': declaration.total_vat_collected,
                'collected_vat_cdf' : declaration.total_vat_collected * declaration.month_exchange_rates,
                'net_vat_usd': declaration.vat_payable,
                'net_vat_cdf': declaration.vat_payable * declaration.month_exchange_rates,
                'declaration_state': declaration.state,
            }

            total_deductible_vat_usd += declaration.total_deductible_vat
            total_deductible_vat_cdf += declaration.total_deductible_vat * declaration.month_exchange_rates
            total_ca_realise_usd += total_ca_usd
            total_ca_realise_cdf += total_ca_usd  * declaration.month_exchange_rates
            total_ca_imposable_usd += total_taxable_ca_usd
            total_ca_imposable_cdf += total_taxable_ca_usd * declaration.month_exchange_rates
            total_tva_collecte_usd += declaration.total_vat_collected
            total_tva_collecte_cdf += declaration.total_vat_collected * declaration.month_exchange_rates
            total_tva_nette_usd += declaration.vat_payable
            total_tva_nette_cdf += declaration.vat_payable * declaration.month_exchange_rates

            result.append(declaration_info)

        total_declaration_info = {
            'total_deductible_vat_usd':  total_deductible_vat_usd,
            'total_deductible_vat_cdf': total_deductible_vat_cdf,
            'total_ca_realise_usd': total_ca_realise_usd,
            'total_ca_realise_cdf': total_ca_realise_cdf,
            'total_ca_imposable_usd': total_ca_imposable_usd,
            'total_ca_imposable_cdf': total_ca_imposable_cdf,
            'total_tva_collecte_usd': total_tva_collecte_usd,
            'total_tva_collecte_cdf': total_tva_collecte_cdf,
            'total_tva_nette_usd': total_tva_nette_usd,
            'total_tva_nette_cdf': total_tva_nette_cdf,
        }
        total.append(total_declaration_info)

        return [result, total]




    def declaration_infos(self):
        declaration_doc_info = []

        company = self.company_id
        company_nature = company.company_nature
        ca_marchandise = 0
        ca_service = 0

        vat_collected_marchandise = 0
        vat_collected_services = 0
        vat_collected_all = 0
        ca_external_invoices = 0
        va_external_invoices = 0

        total_vat_external_importation = 0
        total_vat_local_importation = 0



        lines = self.env['account.move.line'].search([
            ('company_id', '=', self.company_id.id),
            ('invoice_date', '>=', self.start_date),
            ('move_type', '=', 'out_invoice'),
            ('invoice_date', '<=', self.end_date)])

        external_invoices = self.env['account.move'].search([
            ('company_id', '=', self.company_id.id),
            ('invoice_date', '>=', self.start_date),
            ('move_type', '=', 'in_invoice'),
            ('payment_state', 'in', ['posted', 'paid', 'partial', 'in_payment']),
            ('invoice_date', '<=', self.end_date)])

        importation_invoices = self.env['account.move'].search([
            ('company_id', '=', self.company_id.id),
            ('invoice_date', '>=', self.start_date),
            ('move_type', '=', 'in_invoice'),
            ('payment_state', 'in', ['posted', 'paid', 'partial', 'in_payment']),
            ('invoice_date', '<=', self.end_date)])



        if company_nature:
            if company_nature == 'marchandise':
                for line in lines:
                    if line.move_id.payment_state in ['posted', 'paid', 'partial', 'in_payment']:
                        if line.product_id.product_tmpl_id.detailed_type == 'consu':
                            ca_marchandise += line.price_total
                            vat_collected_marchandise += line.price_total - line.price_subtotal

            elif company_nature == 'services':
                for line in lines :
                    if line.move_id.payment_state in ['posted', 'paid', 'partial', 'in_payment']:
                        if line.product_id.product_tmpl_id.detailed_type == 'service':
                            ca_service += line.price_total
                            vat_collected_services += line.price_total - line.price_subtotal

            else:
                for line in lines:
                    if line.move_id.payment_state in ['posted', 'paid', 'partial', 'in_payment']:
                        if line.product_id.product_tmpl_id.detailed_type == 'consu':
                            ca_marchandise += line.price_total
                            vat_collected_marchandise += line.price_total - line.price_subtotal
                        elif line.product_id.product_tmpl_id.detailed_type == 'service':
                            ca_service += line.price_total
                            vat_collected_services += line.price_total - line.price_subtotal



        for invoice in external_invoices :
            if invoice.partner_id.country_id != company.country_id:
                ca_external_invoices += invoice.amount_total_signed
                va_external_invoices += invoice.amount_tax_signed

        ca_external_importation = 0
        ca_local_importation = 0
        for invoice in importation_invoices:
            if invoice.partner_id.country_id != company.country_id:
                total_vat_external_importation += invoice.amount_tax_signed
                ca_external_importation += invoice.amount_total_signed
            else:
                total_vat_local_importation += invoice.amount_tax_signed
                ca_local_importation += invoice.amount_total_signed

        total_vat_importation = total_vat_local_importation + total_vat_local_importation

        declaration_doc_info.append({
            'company_name' : company.name,
            'company_nature' : company_nature,
            'ca_marchandise' : ca_marchandise,
            'ca_service' : ca_service,
            'vat_collected_service' : vat_collected_services,
            'vat_collected_marchandise' : vat_collected_marchandise,
            'total_ca': ca_service + ca_marchandise ,
            'vat_total' :  vat_collected_services + vat_collected_marchandise + vat_collected_all,
            'ca_external_invoice'  : ca_external_invoices,
            'vat_external_invoice' : va_external_invoices,
            'ca_local_importation' : ca_local_importation,
            'ca_external_importation' : ca_external_importation,
            'total_vat_external_importation' : total_vat_external_importation,
            'total_vat_local_importation' : total_vat_local_importation,
            'total_vat_importation' : total_vat_importation,
            'total_deductible_vat' : total_vat_importation,
            'report_preced_credi' : self.last_declaration.vat_credit,
            'total_deductible_bat' : self.total_deductible_vat,
            'total_vat_payable' : self.vat_payable,
            'vat_credit' : self.vat_credit,
            'amount_payable' : self.vat_payable,
        })

        return  declaration_doc_info


    def write_invoice_state(self):

        sales_invoices = self.sales_invoices
        purchases_invoices = self.purchases_invoices
        foreign_supplier_invoices = self.liquidation_statement.foreign_supplier_invoices
        transport_invoices = self.liquidation_statement.transport_invoices
        insurance_invoices = self.liquidation_statement.insurance_invoices
        other_invoices = self.liquidation_statement.other_invoices

        if sales_invoices:
            for invoice in sales_invoices:
                self.change_invoice_state(invoice)

        if purchases_invoices:
            for invoice in purchases_invoices:
                self.change_invoice_state(invoice)

        if foreign_supplier_invoices:
            for invoice in foreign_supplier_invoices:
                self.change_invoice_state(invoice)

        if transport_invoices:
            for invoice in transport_invoices:
                self.change_invoice_state(invoice)

        if insurance_invoices:
            for invoice in insurance_invoices:
                self.change_invoice_state(invoice)

        if other_invoices:
            for invoice in other_invoices:
                self.change_invoice_state(invoice)


    def change_invoice_state(self, invoice):
        invoice.write({'declaration_month': self.mois, 'declaration_state': True})


    def get_bulletin_liquidation_infos(self):

        bulletins_infos = []

        total_bulletin_ht_usd = 0
        total_bulletin_ht_cdf = 0 
        total_vat_bulletin_usd = 0 
        total_vat_bulletin_cdf = 0


        
        for bulletin in self.liquidation_statement :
            bulletin_data = {
                'reference': bulletin.liquidation_statement_reference,
                'date': bulletin.date,
                'montant_ht_usd': bulletin.total_amount_invoice,
                'montant_ht_cdf': bulletin.total_amount_invoice * self.month_exchange_rates,
                'total_tva_usd': bulletin.total_vat,
                'total_tva_ccdf': bulletin.total_vat * self.month_exchange_rates,
            }

            total_bulletin_ht_usd += bulletin.total_amount_invoice
            total_bulletin_ht_cdf += bulletin.total_amount_invoice * self.month_exchange_rates
            total_vat_bulletin_usd += bulletin.total_vat
            total_vat_bulletin_cdf += bulletin.total_vat * self.month_exchange_rates

            bulletins_infos.append(bulletin_data)
        
        self.total_vat_bulletin_usd = total_vat_bulletin_usd
        self.total_vat_bulletin_cdf = total_vat_bulletin_cdf
        self.total_bulletin_ht_usd = total_bulletin_ht_usd
        self.total_bulletin_ht_cdf = total_bulletin_ht_cdf

        return bulletins_infos




class AcountMove(models.Model):
    _inherit = 'account.move'
    invoice_month = fields.Char("Mois de la facture", compute="_compute_month")
    declaration_month = fields.Char("Mois de la déclaration")
    declaration_state = fields.Boolean("Est liée à une déclaration", default=False)
    liquidation_statement_reference = fields.Char('Bulletin de liquidation')

    @api.depends('invoice_date')
    def _compute_month(self):
        month = self.invoice_date.strftime('%B')
        return month



