from odoo import models, api, fields
from datetime import datetime


class ControlDocumentDashboard(models.Model):
    _name = 'control.document.dashboard'
    _description = 'Control Document Dashboard'

    @api.model
    def get_all_data(self):
        return {
            'atd': self.get_all_atd(),
            'avis_de_verification': self.get_all_avis_verification(),
            'contrainte': self.get_all_contrainte(),
            'notification_penal': self.get_all_notification_penal(),
            'amrs': self.get_all_amrs(),
            'med': self.get_all_med(),
            'avis_taxation': self.get_all_avis_taxation(),
            'invitation_serv': self.get_all_invitation_serv(),
            'avis_regulation': self.get_all_regulation(),
            'demande_renseign': self.get_all_demand_renseign(),
            'dgrad': self.get_all_dgdrad(),
            'economie': self.get_all_economie(),
            'environement': self.get_all_environnement(),
            'inspection_travail': self.get_all_inspection_travail(),
            'cotisation_soc_autres': 0,
            'declarations': 0,
            'descente_terrain': 0,
            'rdv_prospection': 0,
            'avis_technique': 0,
            'tache_en_cours': self.get_task_in_progress()
        }

    def get_all_atd(self):
        atd_id = self.env.ref('bvortex_controls.atd_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', atd_id)])

    def get_all_avis_verification(self):
        avis_verification = self.env.ref('bvortex_controls.avis_verification_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', avis_verification)])

    def get_all_contrainte(self):
        contrainte = self.env.ref('bvortex_controls.contrainte_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', contrainte)])

    def get_all_notification_penal(self):
        contrainte = self.env.ref('bvortex_controls.notification_penalites_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', contrainte)])

    def get_all_amrs(self):
        arms = self.env.ref('bvortex_controls.amrs_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', arms)])

    def get_all_med(self):
        med = self.env.ref('bvortex_controls.mise_demeure_declarer_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', med)])

    def get_all_avis_taxation(self):
        avis_taxation = self.env.ref('bvortex_controls.avis_taxation_office_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', avis_taxation)])

    def get_all_invitation_serv(self):
        invitation_serv = self.env.ref('bvortex_controls.invitation_service_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', invitation_serv)])

    def get_all_regulation(self):
        regulation = self.env.ref('bvortex_controls.regularisation_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', regulation)])

    def get_all_demand_renseign(self):
        demand_renseign = self.env.ref('bvortex_controls.demande_justification_code_nature').id
        document_fiscal = self.get_all_document_fiscal()

        return document_fiscal.search_count([('nature_id', '=', demand_renseign)])

    def get_all_dgdrad(self):
        dgdrad = self.env.ref('bvortex_controls.dgrad_code_minister').id
        document_prefiscal = self.get_all_document_fiscal()

        return document_prefiscal.search_count([('minister_id', '=', dgdrad)])

    def get_all_economie(self):
        economie = self.env.ref('bvortex_controls.economie_code_minister').id
        document_prefiscal = self.get_all_document_fiscal()

        return document_prefiscal.search_count([('minister_id', '=', economie)])

    def get_all_environnement(self):
        environnement = self.env.ref('bvortex_controls.environnement_code_minister').id
        document_prefiscal = self.get_all_document_fiscal()

        return document_prefiscal.search_count([('minister_id', '=', environnement)])

    def get_all_inspection_travail(self):
        inspection_travail = self.env.ref('bvortex_controls.inspection_travail_code_minister').id
        document_prefiscal = self.get_all_document_fiscal()

        return document_prefiscal.search_count([('minister_id', '=', inspection_travail)])



    def get_task_in_progress(self):
        current_date_time = fields.Datetime.now()
        return len(self.env['project.task'].search([('date_deadline', '>=', current_date_time)]))

    def get_all_document_spontanne(self):
        return self.env['control.document'].search([('category', '=', 'spontanne')])

    def get_all_document_fiscal(self):
        return self.env['control.document'].search([('category', '=', 'fiscal')])

    def get_all_document_parafiscal(self):
        return self.env['control.document'].search([('category', '=', 'parafiscal')])





