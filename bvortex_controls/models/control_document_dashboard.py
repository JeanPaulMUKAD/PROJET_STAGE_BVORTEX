from odoo import models, api


class ControlDocumentDashboard(models.Model):
    _name = 'control.document.dashboard'
    _description = 'Control Document Dashboard'

    @api.model
    def get_all_data(self):
        return {
            'atd': 0,
            'avis_de_verification': 0,
            'contrainte': 0,
            'notification_penal': 0,
            'amrs': 0,
            'med': 0,
            'avis_taxation': 0,
            'invitation_serv': 0,
            'avis_regulation': 0,
            'demande_renseign': 0,
            'dgrad': 0,
            'economie': 0,
            'environement': 0,
            'inspection_travail': 0,
            'cotisation_soc_autres': 0,
            'declarations': 0,
            'descente_terrain': 0,
            'rdv_prospection': 0,
            'avis_technique': 0,
            'tache_en_cours': 0
        }
