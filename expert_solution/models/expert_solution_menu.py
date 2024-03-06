# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpertSolutionMenu(models.Model):
    _name = "expert_menu"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

    def print_report(self):
        pass