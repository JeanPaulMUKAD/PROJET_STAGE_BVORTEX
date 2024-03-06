# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpertSolutionMenu(models.Model):
    _name = "declaration_tva"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

    def print_report(self):
        pass