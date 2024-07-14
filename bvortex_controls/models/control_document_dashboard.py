from odoo import models, api, _


class ControlDocumentDashboard(models.Model):
    _name = 'control.document.dashboard'
    _description = 'Control Document Dashboard'

    @api.model
    def on_link_click(self, id):
        if id == 'atd_click':
            atd = self.env.ref('bvortex_controls.atd_code_nature').id
            return self.go_to_nature(atd)
        elif id == 'avis_de_verification_click':
            avis_verification = self.env.ref('bvortex_controls.avis_verification_code_nature').id
            return self.go_to_nature(avis_verification)
        elif id == 'contrainte_click':
            contrainte = self.env.ref('bvortex_controls.contrainte_code_nature').id
            return self.go_to_nature(contrainte)
        elif id == 'notification_penal_click':
            notification_penal = self.env.ref('bvortex_controls.notification_penalites_code_nature').id
            return self.go_to_nature(notification_penal)
        elif id == 'amrs_click':
            arms = self.env.ref('bvortex_controls.amrs_code_nature').id
            return self.go_to_nature(arms)
        elif id == 'med_click':
            med = self.env.ref('bvortex_controls.mise_demeure_declarer_code_nature').id
            return self.go_to_nature(med)
        elif id == 'avis_taxation_click':
            avis_taxation = self.env.ref('bvortex_controls.avis_taxation_office_code_nature').id
            return self.go_to_nature(avis_taxation)
        elif id == 'invitation_serv_click':
            invitation_serv = self.env.ref('bvortex_controls.invitation_service_code_nature').id
            return self.go_to_nature(invitation_serv)
        elif id == 'avis_regulation_click':
            regulation = self.env.ref('bvortex_controls.regularisation_code_nature').id
            return self.go_to_nature(regulation)
        elif id == 'demande_renseign_click':
            demand_renseign = self.env.ref('bvortex_controls.demande_justification_code_nature').id
            return self.go_to_nature(demand_renseign)
        elif id == 'dgrad_click':
            dgdrad = self.env.ref('bvortex_controls.dgrad_code_minister').id
            return self.go_to_minister(dgdrad)
        elif id == 'economie_click':
            economie = self.env.ref('bvortex_controls.economie_code_minister').id
            return self.go_to_minister(economie)
        elif id == 'environement_click':
            environnement = self.env.ref('bvortex_controls.environnement_code_minister').id
            return self.go_to_minister(environnement)
        elif id == 'inspection_travail_click':
            inspection_travail = self.env.ref('bvortex_controls.inspection_travail_code_minister').id
            return self.go_to_minister(inspection_travail)
        elif id == 'cotisation_soc_autres_click':
            cotisation_soc_autres = self.env.ref('bvortex_controls.cotisation_soc_autres_code_action').id
            return self.go_to_action(cotisation_soc_autres)
        elif id == 'declarations_click':
            declaration = self.env.ref('bvortex_controls.declarations_code_action').id
            return self.go_to_action(declaration)
        elif id == 'descente_terrain_click':
            descente_terrain = self.env.ref('bvortex_controls.descente_terrain_code_action').id
            return self.go_to_action(descente_terrain)
        elif id == 'rdv_prospection_click':
            rdv_prospection = self.env.ref('bvortex_controls.rdv_prospection_code_action').id
            return self.go_to_action(rdv_prospection)
        elif id == 'avis_technique_click':
            avis_technique = self.env.ref('bvortex_controls.avis_technique_code_action').id
            return self.go_to_action(avis_technique)
        elif id == 'tache_en_cours_click':
            return self.go_to_task()

    def go_to_nature(self, nature_id):
        return {
            'name': "Control Document",
            'res_model': "control.document",
            'views': [[False, "tree"]],
            'type': "ir.actions.act_window",
            'domain': [('nature_id', '=', nature_id)],
            'view_mode': "tree"
        }

    def go_to_minister(self, minister_id):
        return {
            'name': "Control Document",
            'res_model': "control.document",
            'views': [[False, "tree"]],
            'type': "ir.actions.act_window",
            'domain': [('minister_id', '=', minister_id)],
            'view_mode': "tree"
        }

    def go_to_action(self, action_id):
        progress_state = self.env.ref('bvortex_controls.in_progress_stage').id
        return {
            'name': "Toutes les taches",
            'res_model': "project.task",
            'views': [[False, "tree"]],
            'type': "ir.actions.act_window",
            'domain': [('action_id', '=', action_id), ('stage_id', '=', progress_state)],
            'view_mode': "tree"
        }

    def go_to_task(self):
        progress_state = self.env.ref('bvortex_controls.in_progress_stage').id
        return {
            'name': "Toutes les taches",
            'res_model': "project.task",
            'views': [[False, "tree"]],
            'type': "ir.actions.act_window",
            'domain': [('stage_id', '=', progress_state)],
            'view_mode': "tree"
        }

    @api.model
    def get_all_data(self):
        declaration = self.env.ref('bvortex_controls.declarations_code_action').id
        cotisation_soc_autres = self.env.ref('bvortex_controls.cotisation_soc_autres_code_action').id
        descente_terrain = self.env.ref('bvortex_controls.descente_terrain_code_action').id
        rdv_prospection = self.env.ref('bvortex_controls.rdv_prospection_code_action').id
        avis_technique = self.env.ref('bvortex_controls.avis_technique_code_action').id

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
            'cotisation_soc_autres': self.get_all_action_by_type(cotisation_soc_autres),
            'declarations': self.get_all_action_by_type(declaration),
            'descente_terrain': self.get_all_action_by_type(descente_terrain),
            'rdv_prospection': self.get_all_action_by_type(rdv_prospection),
            'avis_technique': self.get_all_action_by_type(avis_technique),
            'tache_en_cours': self.get_all_tasks()
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

    def get_all_action_by_type(self, action):
        quantity = 0
        tasks = self.env['project.task'].search([('action_id', '=', action)])
        for task in tasks:
            if self.is_in_progress(task):
                quantity += 1

        return 0

    def get_all_document_spontanne(self):
        return self.env['control.document'].search([('category', '=', 'spontanne')])

    def get_all_document_fiscal(self):
        return self.env['control.document'].search([('category', '=', 'fiscal')])

    def get_all_document_parafiscal(self):
        return self.env['control.document'].search([('category', '=', 'parafiscal')])

    def get_all_tasks(self):
        document_in_progress = self.env['control.document'].search([('state', '=', 'in_progress')])
        tasks = 0
        for document in document_in_progress:
            for task in document.task_ids:
                if self.is_in_progress(task):
                    tasks += 1

        return tasks

    def is_in_progress(self, task):
        return task.stage_id.id == self.env.ref('bvortex_controls.in_progress_stage').id
