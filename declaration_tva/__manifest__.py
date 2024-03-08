# -*- coding: utf-8 -*-
{
    'name': "declaration_tva",

    'summary': "Expert soluition for accounting TVA",

    'description': """
Long description of module's purpose
    """,

    'author': "bvortex",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '17.0',

    'depends': ['base', 'account_accountant','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/views_declaration_tva.xml',
        'views/new_declaration.xml',
        'report/declaration_report.xml',
        'report/vat_recap_report.xml',
        'report/vat_synthese_report.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,

}

