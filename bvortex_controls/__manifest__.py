# -*- coding: utf-8 -*-
{
    'name': "Fiscal Controls",

    'summary': "Expert soluition for declarations, fiscal controls",

    'description': """
            
    """,

    'author': "Bvortex",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '17.0',

    'depends': ['base', 'mail', 'project', 'web'],

    'data': [
        'security/ir.model.access.csv',
        'security/fiscal_groups.xml',
        'security/ir_rules.xml',
        'data/ir_sequence_data.xml',
        'data/ir_minister_data.xml',
        'data/ir_nature_data.xml',
        'data/ir_action_data.xml',
        'data/activity_document.xml',
        'data/email_document.xml',
        'data/cron.xml',
        'data/ir_project_task_type_data.xml',
        'views/menu.xml',
        'views/control_nature.xml',
        'views/control_minister.xml',
        'views/control_document.xml',
        'views/coontrol_planingue.xml',
        'views/coontrol_planingue_line.xml',
        'views/coontrol_planingue_taches.xml',
        'views/control_action.xml',
        'views/project_task.xml',
    ],
    'images': ['bvortex_controls/static/description/icon.png'],
    'assets': {
        'web.assets_backend': [
            'bvortex_controls/static/src/js/dashboard.js',
            'bvortex_controls/static/src/xml/dashboard.xml',
        ],
    },
    'application': True,
    'installable': True,
}
