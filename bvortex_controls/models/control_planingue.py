from odoo import api, fields, models, exceptions, _
from datetime import datetime
from odoo.http import request


class Control_Planingue(models.Model):
    _name = 'control.planingue'

    partner_id = fields.Many2one('res.partner', string="Customer", domain=[('is_company', '=', True)])
    #task_ids = fields.One2many('project.task', 'planingue_id', string="Tasks")
    #project_ids = fields.One2many('project.project', 'document_id', string="project")
    task_count = fields.Integer(compute='task_compute_count')
    project_count = fields.Integer(compute='project_compute_count')

    code = fields.Char('Code', readonly=True )
    nom = fields.Char('Nom')
    date_debut = fields.Date('Date debut')
    date_fin = fields.Date('Date fin')
    statut = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Statut', required=True , copy=False,
        tracking=True, default='draft')
    planingue_line_ids = fields.One2many('control.planingue.line','planingue_id','ligne des planingues')
    planingue_report_ids = fields.One2many('control.planingue.report','planingue_id','ligne des report')
    project_ids = fields.One2many('project.project','planingue_id')

    def get_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.task',
            'domain': [('project_id', 'in', self.project_ids.ids)],
            'context': {
                'create': True,
                'default_partner_id': self.partner_id.id,
                'default_planingue_id': self.id,
            }
        }

    def task_compute_count(self):
        for record in self:
            record.task_count = self.env['project.task'].search_count([('project_id', 'in', self.project_ids.ids)])



    def get_project(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'project',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.project',
            'domain': [('id', 'in', self.project_ids.ids)],
            'context': {
                'create': True,
                'default_partner_id': self.partner_id.id,
                'default_planingue_id': self.id,
            }
        }

    def project_compute_count(self):
        for record in self:
            record.project_count = record.env['project.project'].search_count([('id', 'in', record.project_ids.ids)])

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('control.planingue') or 'PLAN'
            msg_body = 'Control Planingue Created'
            for msg in self:
                msg.message_post(body=msg_body)
            result = super(Control_Planingue, self).create(vals_list)
        return result

    def action_confirmed(self):
        #  mail n*1
        mail_values = {
            'email_to': rec.get_fiscal_manager_user().email,
            'subject': 'Contrôles de' ,
            'body_html': f"""
                                  <p>Bonjour cher manager {rec.get_fiscal_manager_user().name},</p>
                                  <p>Je vous prie de trouver en annexe le rapport mensuel sur les contrôleurs.</p>
                              """,
        }

        if rec.get_emails_for_department_head():
            mail_vals['email_cc'] = rec.get_emails_for_department_head()

        mail = self.env['mail.mail'].sudo().create(mail_values)
        mail.send()

        # mail n*2

        mail2_values = {
            'email_to': rec.get_fiscal_manager_user().email,
            'subject': 'déclarations fiscales de' ,
            'body_html': f"""
                                      <p>Bonjour cher manager {rec.get_fiscal_manager_user().name},</p>
                                      <p>Je vous prie de trouver en annexe  mensuel sur les déclarations avec  les différents statuts de chaque impôt ou taxe</p>
                                      <p>Cordialement <p/>
                                          """,
        }

        if rec.get_emails_for_department_head():
            mail2_vals['email_cc'] = rec.get_emails_for_department_head()

        mail2 = self.env['mail.mail'].sudo().create(mail2_values)
        mail2.send()

        # mail n*3

        mail3_values = {
            'email_to': rec.get_fiscal_manager_user().email,
            'subject': 'taches du mois de' ,
            'body_html': f"""
                                  <p>Bonjour cher manager {rec.get_fiscal_manager_user().name},</p>
                                  <p>Je vous prie de trouver en annexe, le rapport mensuel sur les taches mensuelles  du mois, lesquels répartissent, les taches prévues, effectuées et celles en cours par département, collaborateur et projet.</p>
                                  <p>Cordialement <p/>
                                     """,
        }

        if rec.get_emails_for_department_head():
            mail3_vals['email_cc'] = rec.get_emails_for_department_head()

        mail3 = self.env['mail.mail'].sudo().create(mail3_values)
        mail3.send()


        for record in self:

            planingue_line_ids = record.planingue_line_ids

            if planingue_line_ids:
                record.statut = 'confirmed'
            else:
                raise exceptions.UserError(_("veillez specifier les lignes de planingue."))

    def action_in_progress(self):
        for record in self:
            record.statut = 'in_progress'
            code = record.code
            planingue_line_ids = record.planingue_line_ids
            planingue_report_ids = record.planingue_report_ids



        for planingue_line in self.planingue_line_ids:

            now = datetime.now()
            current_month = now.month
            current_year = now.year
            month_name = now.strftime('%B').upper()  # Nom complet du mois, ex: August
            year = now.strftime('%Y')

            start_date = f'{current_year}-{current_month:02d}-01'
            end_date = f'{current_year}-{current_month:02d}-31'

            project = self.env['project.project'].search([
                '|', '|',
                ('date_start', '<=', end_date),
                ('date', '>=', start_date),
                ('date_start', '>=', start_date),
                ('date', '<=', end_date),
                ('partner_id', '=' ,planingue_line.client.id )
            ])

            if not project:
                vals = {
                    'name': code + "-" + str(planingue_line.client.name).upper() + '-' + month_name + '-' + year,
                    'user_id': self.env.user.id,
                    'partner_id': planingue_line.client.id,
                    'date_start': start_date,
                    'date': end_date ,
                    'planingue_id': self.id
                }
                project = self.env['project.project'].create(vals)

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.draft_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.etablie_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.revue_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.validée_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.payé_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.déclarée_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.apuré_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.archivé_stage').id)],
                })

                project.write({
                    'type_ids': [(4, self.env.ref('bvortex_controls.transmis_stage').id)],
                })

            else:
                project.write({
                    'planingue_id': [(4, self.id)]  # Ajoute l'ID actuel au champ Many2many
                })
            for planingue_taches in self.planingue_line_ids.planingue_taches_ids:
                vals = {
                    'name': planingue_taches.nom,
                    'project_id': project.id,
                    'user_ids': planingue_taches.utilisateur,
                    'date_deadline': planingue_taches.date,
                    'task_task': planingue_taches.id,
                    'statut_ch': planingue_line_ids.id
                }
                task = self.env['project.task'].create(vals)

        for planingue_report in self.planingue_report_ids:

            now = datetime.now()
            current_month = now.month
            current_year = now.year
            month_name = now.strftime('%B').upper()  # Nom complet du mois, ex: August
            year = now.strftime('%Y')

            start_date = f'{current_year}-{current_month:02d}-01'
            end_date = f'{current_year}-{current_month:02d}-31'

            project = self.env['project.project'].search([
                '|', '|',
                ('date_start', '<=', end_date),
                ('date', '>=', start_date),
                ('date_start', '>=', start_date),
                ('date', '<=', end_date),
                ('partner_id', '=' ,planingue_report.client.id )
            ])

            if planingue_report_ids :

                    if not project:
                        vals = {
                            'name': code + "-" + str(planingue_report.client.name).upper() + '-' + month_name + '-' + year,
                            'user_id': self.env.user.id,
                            'partner_id': planingue_report.client.id,
                            'date_start': start_date,
                            'date': end_date ,
                            'planingue_id': self.id
                        }
                        project = self.env['project.project'].create(vals)

                        type_ids = []

                        for step in self.planingue_report_ids.etape:
                            if step.id:
                                type_ids.append(step.id)

                        project.write({
                            'type_ids': [(6, 0, type_ids)]
                        })

                    else:
                        project.write({
                            'planingue_id': [(4, self.id)]  # Ajoute l'ID actuel au champ Many2many
                        })
                    for planingue_taches in self.planingue_report_ids.planingue_taches_ids:
                        vals = {
                            'name': planingue_taches.nom,
                            'project_id': project.id,
                            'user_ids': planingue_taches.utilisateur,
                            'date_deadline': planingue_taches.date,
                            'task_task': planingue_taches.id,
                            'statut_ch': planingue_report_ids.id
                        }
                        task = self.env['project.task'].create(vals)


    def action_draft(self):
        for rec in self:
            rec.statut = 'draft'

    def action_done(self):
        for rec in self:
            rec.statut = 'done'

    def action_cancel(self):
      for rec in self:
          rec.statut = 'cancel'









