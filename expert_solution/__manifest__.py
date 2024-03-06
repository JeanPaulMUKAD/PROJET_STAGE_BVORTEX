# -*- coding: utf-8 -*-
{
    'name': "expert_solution",

    'summary': "Expert soluition for accounting TVA",

    'description': """
Long description of module's purpose
    """,

    'author': "bvortex",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '17.0',

    'depends': ['base', 'account_accountant'],

    'data': [
        'security/ir.model.access.csv',
        'views/expert_solution_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,

}

