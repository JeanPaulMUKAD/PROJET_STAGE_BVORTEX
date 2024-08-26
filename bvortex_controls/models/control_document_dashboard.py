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





        elif id == 'etablie_click':
            return self.go_to_planingue()
        elif id == 'revue_click':
            return self.go_to_planingue2()
        elif id == 'valider_click':
            return self.go_to_planingue3()
        elif id == 'payer_click':
            return self.go_to_planingue4()
        elif id == 'déclarer_click':
            return self.go_to_planingue5()
        elif id == 'apurer_click':
            return self.go_to_planingue6()
        elif id == 'archiver_click':
            return self.go_to_planingue7()
        elif id == 'transmis_click':
            return self.go_to_planingue8()

        elif id == 'etablie2_click':
            return self.go_to_planingue9()
        elif id == 'revue2_click':
            return self.go_to_planingue10()
        elif id == 'valider2_click':
            return self.go_to_planingue11()
        elif id == 'payer2_click':
            return self.go_to_planingue12()
        elif id == 'déclarer2_click':
            return self.go_to_planingue13()
        elif id == 'apurer2_click':
            return self.go_to_planingue14()
        elif id == 'archiver2_click':
            return self.go_to_planingue15()
        elif id == 'transmis2_click':
            return self.go_to_planingue16()

        elif id == 'etablie3_click':
            return self.go_to_planingue17()
        elif id == 'revue3_click':
            return self.go_to_planingue18()
        elif id == 'valider3_click':
            return self.go_to_planingue19()
        elif id == 'payer3_click':
            return self.go_to_planingue20()
        elif id == 'déclarer3_click':
            return self.go_to_planingue21()
        elif id == 'apurer3_click':
            return self.go_to_planingue22()
        elif id == 'archiver3_click':
            return self.go_to_planingue23()
        elif id == 'transmis3_click':
            return self.go_to_planingue24()

        elif id == 'etablie4_click':
            return self.go_to_planingue25()
        elif id == 'revue4_click':
            return self.go_to_planingue26()
        elif id == 'valider4_click':
            return self.go_to_planingue27()
        elif id == 'payer4_click':
            return self.go_to_planingue28()
        elif id == 'déclarer4_click':
            return self.go_to_planingue29()
        elif id == 'apurer4_click':
            return self.go_to_planingue30()
        elif id == 'archiver4_click':
            return self.go_to_planingue31()
        elif id == 'transmis4_click':
            return self.go_to_planingue32()
        
        elif id == 'etablie5_click':
            return self.go_to_planingue33()
        elif id == 'revue5_click':
            return self.go_to_planingue34()
        elif id == 'valider5_click':
            return self.go_to_planingue35()
        elif id == 'payer5_click':
            return self.go_to_planingue36()
        elif id == 'déclarer5_click':
            return self.go_to_planingue37()
        elif id == 'apurer5_click':
            return self.go_to_planingue38()
        elif id == 'archiver5_click':
            return self.go_to_planingue39()
        elif id == 'transmis5_click':
            return self.go_to_planingue40()
        
        elif id == 'etablie6_click':
            return self.go_to_planingue41()
        elif id == 'revue6_click':
            return self.go_to_planingue42()
        elif id == 'valider6_click':
            return self.go_to_planingue43()
        elif id == 'payer6_click':
            return self.go_to_planingue44()
        elif id == 'déclarer6_click':
            return self.go_to_planingue45()
        elif id == 'apurer6_click':
            return self.go_to_planingue46()
        elif id == 'archiver6_click':
            return self.go_to_planingue47()
        elif id == 'transmis6_click':
            return self.go_to_planingue48()

        elif id == 'etablie7_click':
            return self.go_to_planingue49()
        elif id == 'revue7_click':
            return self.go_to_planingue50()
        elif id == 'valider7_click':
            return self.go_to_planingue51()
        elif id == 'payer7_click':
            return self.go_to_planingue52()
        elif id == 'déclarer7_click':
            return self.go_to_planingue53()
        elif id == 'apurer7_click':
            return self.go_to_planingue54()
        elif id == 'archiver7_click':
            return self.go_to_planingue55()
        elif id == 'transmis7_click':
            return self.go_to_planingue56()




    def go_to_planingue(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'ONEM')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue2(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'ONEM')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue3(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue4(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue5(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue6(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue7(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue8(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'ONEM')
            ],
            'view_mode': "tree"
        }






    def go_to_planingue9(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'INPP')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue10(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'INPP')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue11(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue12(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue13(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue14(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue15(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue16(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'INPP')
            ],
            'view_mode': "tree"
        }



    def go_to_planingue17(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'CNSS')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue18(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'CNSS')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue19(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue20(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue21(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue22(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue23(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue24(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'CNSS')
            ],
            'view_mode': "tree"
        }


    def go_to_planingue25(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'MINECO')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue26(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'MINECO')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue27(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue28(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue29(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue30(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue31(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue32(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'MINECO')
            ],
            'view_mode': "tree"
        }
    
    

    def go_to_planingue33(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'etablie'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue34(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'revue'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue35(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'valider'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue36(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'payer'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue37(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'déclarer'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue38(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'apurer'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue39(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'archiver'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }

    def go_to_planingue40(self):
            return {
                'name': "Toutes les planingue",
                'res_model': "control.planingue.line",
                'views': [[False, "tree"], [False, "form"]],
                'type': "ir.actions.act_window",
                'domain': [
                    '&',
                    ('statut', '=', 'transmis'),
                    ('type_selct', '=', 'INDUSTRIE')
                ],
                'view_mode': "tree"
            }
        
    def go_to_planingue41(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'IPR')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue42(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'IPR')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue43(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue44(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue45(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue46(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue47(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue48(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'IPR')
            ],
            'view_mode': "tree"
        }

       
       
       
    def go_to_planingue49(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'etablie'),
                ('type_selct', '=', 'TVA')
                ],
            'view_mode': "tree"
            }
    def go_to_planingue50(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'revue'),
                ('type_selct', '=', 'TVA')
                ],
            'view_mode': "tree"
            }

    def go_to_planingue51(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'valider'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue52(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'payer'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue53(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'déclarer'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue54(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'apurer'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue55(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'archiver'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }

    def go_to_planingue56(self):
        return {
            'name': "Toutes les planingue",
            'res_model': "control.planingue.line",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [
                '&',
                ('statut', '=', 'transmis'),
                ('type_selct', '=', 'TVA')
            ],
            'view_mode': "tree"
        }



    def go_to_nature(self, nature_id):
        return {
            'name': "Control Document",
            'res_model': "control.document",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [('nature_id', '=', nature_id)],
            'view_mode': "tree"
        }


    def go_to_minister(self, minister_id):
        return {
            'name': "Control Document",
            'res_model': "control.document",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [('minister_id', '=', minister_id)],
            'view_mode': "tree"
        }

    def go_to_action(self, action_id):
        progress_state = self.env.ref('bvortex_controls.in_progress_stage').id
        return {
            'name': "Toutes les taches",
            'res_model': "project.task",
            'views': [[False, "tree"], [False, "form"]],
            'type': "ir.actions.act_window",
            'domain': [('action_id', '=', action_id), ('stage_id', '=', progress_state)],
            'view_mode': "tree"
        }

    def go_to_task(self):
        progress_state = self.env.ref('bvortex_controls.in_progress_stage').id
        return {
            'name': "Toutes les taches",
            'res_model': "project.task",
            'views': [[False, "tree"], [False, "form"]],
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
            'tache_en_cours': self.get_all_tasks(),


            'etablie_nbr': self.get_all_etablie(),
            'revue_nbr': self.get_all_revue(),
            'valider_nbr': self.get_all_valider(),
            'payer_nbr': self.get_all_payer(),
            'declarer_nbr': self.get_all_declarer(),
            'apurer_nbr': self.get_all_apurer(),
            'archiver_nbr': self.get_all_archiver(),
            'transmit_nbr': self.get_all_transmis(),

            'etablie2_nbr': self.get_all_etablie2(),
            'revue2_nbr': self.get_all_revue2(),
            'valider2_nbr': self.get_all_valider2(),
            'payer2_nbr': self.get_all_payer2(),
            'declarer2_nbr': self.get_all_declarer2(),
            'apurer2_nbr': self.get_all_apurer2(),
            'archiver2_nbr': self.get_all_archiver2(),
            'transmit2_nbr': self.get_all_transmis2(),

            'etablie3_nbr': self.get_all_etablie3(),
            'revue3_nbr': self.get_all_revue3(),
            'valider3_nbr': self.get_all_valider3(),
            'payer3_nbr': self.get_all_payer3(),
            'declarer3_nbr': self.get_all_declarer3(),
            'apurer3_nbr': self.get_all_apurer3(),
            'archiver3_nbr': self.get_all_archiver3(),
            'transmit3_nbr': self.get_all_transmis3(),

            'etablie4_nbr': self.get_all_etablie4(),
            'revue4_nbr': self.get_all_revue4(),
            'valider4_nbr': self.get_all_valider4(),
            'payer4_nbr': self.get_all_payer4(),
            'declarer4_nbr': self.get_all_declarer4(),
            'apurer4_nbr': self.get_all_apurer4(),
            'archiver4_nbr': self.get_all_archiver4(),
            'transmit4_nbr': self.get_all_transmis4(),

            'etablie5_nbr': self.get_all_etablie5(),
            'revue5_nbr': self.get_all_revue5(),
            'valider5_nbr': self.get_all_valider5(),
            'payer5_nbr': self.get_all_payer5(),
            'declarer5_nbr': self.get_all_declarer5(),
            'apurer5_nbr': self.get_all_apurer5(),
            'archiver5_nbr': self.get_all_archiver5(),
            'transmit5_nbr': self.get_all_transmis5(),

            'etablie6_nbr': self.get_all_etablie6(),
            'revue6_nbr': self.get_all_revue6(),
            'valider6_nbr': self.get_all_valider6(),
            'payer6_nbr': self.get_all_payer6(),
            'declarer6_nbr': self.get_all_declarer6(),
            'apurer6_nbr': self.get_all_apurer6(),
            'archiver6_nbr': self.get_all_archiver6(),
            'transmit6_nbr': self.get_all_transmis6(),

            'etablie7_nbr': self.get_all_etablie7(),
            'revue7_nbr': self.get_all_revue7(),
            'valider7_nbr': self.get_all_valider7(),
            'payer7_nbr': self.get_all_payer7(),
            'declarer7_nbr': self.get_all_declarer7(),
            'apurer7_nbr': self.get_all_apurer7(),
            'archiver7_nbr': self.get_all_archiver7(),
            'transmit7_nbr': self.get_all_transmis7(),

        }

    def get_all_etablie(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'),('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'),('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'),('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'ONEM'), ('statut', '=', 'transmis')])
        return document_onem




    def get_all_etablie2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis2(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INPP'), ('statut', '=', 'transmis')])
        return document_onem




    def get_all_etablie3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis3(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'CNSS'), ('statut', '=', 'transmis')])
        return document_onem

    def get_all_etablie4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis4(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'MINECO'), ('statut', '=', 'transmis')])
        return document_onem

    def get_all_etablie5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis5(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'INDUSTRIE'), ('statut', '=', 'transmis')])
        return document_onem





    def get_all_etablie6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis6(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'IPR'), ('statut', '=', 'transmis')])
        return document_onem

    def get_all_etablie7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'etablie')])
        return document_onem

    def get_all_revue7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'revue')])
        return document_onem

    def get_all_valider7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'valider')])
        return document_onem

    def get_all_payer7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'payer')])
        return document_onem

    def get_all_declarer7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'déclarer')])
        return document_onem

    def get_all_apurer7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'apurer')])
        return document_onem

    def get_all_archiver7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'archiver')])
        return document_onem

    def get_all_transmis7(self):
        document_onem = self.env['control.planingue.line'].search_count(
            [('type_selct', '=', 'TVA'), ('statut', '=', 'transmis')])
        return document_onem




















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

        return quantity

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
