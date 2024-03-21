from odoo import models, fields, api

class BulletinLiquidation(models.Model):
    _name = "bulletin_liquidation"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    liquidation_statement_reference = fields.Char("Référence du bulletin de liquidation", required=True, tracking=True)
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
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Bulletin de liquidation validé...',
                'type': 'rainbow_man',
            }
        }

