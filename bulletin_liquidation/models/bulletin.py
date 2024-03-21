from odoo import models, fields, api

class BulletinLiquidation(models.Model):
    _name = "bulletin_liquidation"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    liquidation_statement_reference = fields.Char("Référence", required=True, tracking=True)
    date = fields.Date("Date d'émission", required=True)

    collaborator = fields.Many2one('res.users', string="Collaborateur", required=True)
    company_id = fields.Many2one('res.company', string="Société", required=True)
    state = fields.Selection([('draft', 'Brouillon'), ('save', 'Sauver'), ('done', 'Fait')], default="draft", string='Status')


    total_amount_invoice = fields.Float("Monntant total")
    total_vat = fields.Float("TVA totale")

    foreign_supplier_invoices = fields.Many2many('account.move', 'has_message', string="Factures fournisseur Etranger", required=True)
    transport_invoices = fields.Many2many('account.move', 'always_tax_exigible', string="Factures de transport", required=True)
    insurance_invoices = fields.Many2many('account.move', 'auto_post', string="Factures assurance", required=True)
    other_invoices = fields.Many2many('account.move', string="Autres factures")

    def button_edit(self):
        self.write({'state': 'draft'})

    def button_confirm(self):
        self.write({'state': 'save'})

    def button_done(self):
        self.write({'state': 'done'})
        foreign_supplier_invoices = self.foreign_supplier_invoices
        transport_invoices = self.transport_invoices
        insurance_invoices = self.insurance_invoices
        other_invoices = self.other_invoices

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

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Bulletin de liquidation validé...',
                'type': 'rainbow_man',
            }
        }

    @api.onchange('foreign_supplier_invoices', 'transport_invoices', 'insurance_invoices', 'other_invoices')
    def compute_total_amount_invoice(self):
        tolal_amount_invoice = 0

        foreign_supplier_invoices = self.foreign_supplier_invoices
        transport_invoices = self.transport_invoices
        insurance_invoices = self.insurance_invoices
        other_invoices = self.other_invoices

        if foreign_supplier_invoices:
            for invoice in foreign_supplier_invoices:
                tolal_amount_invoice += invoice.amount_total_signed

        if transport_invoices:
            for invoice in transport_invoices:
                tolal_amount_invoice += invoice.amount_total_signed

        if insurance_invoices:
            for invoice in insurance_invoices:
                tolal_amount_invoice += invoice.amount_total_signed

        if other_invoices:
            for invoice in other_invoices:
                tolal_amount_invoice += invoice.amount_total_signed


        total_tva = tolal_amount_invoice * 0.16


        self.write({'total_amount_invoice': tolal_amount_invoice, 'total_vat' : total_tva})

    def change_invoice_state(self, invoice):
        invoice.write({'liquidation_statement_reference': self.liquidation_statement_reference})