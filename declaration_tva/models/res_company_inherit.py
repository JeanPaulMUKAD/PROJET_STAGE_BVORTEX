# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools

class Company(models.Model):
    _inherit = 'res.company'

    total_collected_vat_account = fields.Many2one('account.account', string="Compte total TVA collectée")
    total_deductible_vat_account = fields.Many2one('account.account', string="Compte total TVA déductibles")
    credit_vat_account = fields.Many2one('account.account', string="Compte crédit TVA")
    vat_payable_account = fields.Many2one('account.account', string="Compte TVA payable")
    other_import_rights = fields.Many2one('account.account', string="Autres droits à l'importation")


    company_nature = fields.Selection([
        ('marchandise', 'Livraisons de biens'),
        ('services', 'Prestations de services'),
        ('all', 'Livraisons de bien et Prestations de services')

    ], string='Nature de la société', required=True)

