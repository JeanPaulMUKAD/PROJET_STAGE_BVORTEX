# -*- coding: utf-8 -*-
{
    'name': "declaration_tva",

    'summary': "DECLARATION TVA",

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
        'views/view_declaration_tva.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,

}

