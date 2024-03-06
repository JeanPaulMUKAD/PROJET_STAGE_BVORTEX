# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Declaration(models.Model):
    _name = "declation_tva"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

    def print_report(self):
        pass