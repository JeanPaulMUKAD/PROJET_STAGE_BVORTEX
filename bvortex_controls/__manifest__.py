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

    'depends': ['base', 'mail', 'project'],

    'data': [
        'security/ir.model.access.csv',
        'security/fiscal_groups.xml',
        'data/ir_sequence_data.xml',
        'data/ir_minister_data.xml',
        'data/ir_nature_data.xml',
        'data/activity_document.xml',
        'views/menu.xml',
        'views/control_nature.xml',
        'views/control_minister.xml',
        'views/control_document.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
}

