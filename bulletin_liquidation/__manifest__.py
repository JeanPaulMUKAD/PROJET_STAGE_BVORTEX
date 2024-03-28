# -*- coding: utf-8 -*-
{
    'name': "bulletin_liquidation",

    'summary': "Expert soluition for liquidation buelletin",

    'description': """
Long description of module's purpose
    """,

    'author': "bvortex",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '17.0',

    'depends': ['base', 'account_accountant', 'sale_management', 'purchase', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/new_bulletin.xml',
        'views/view_bulletin_liquidation.xml',

    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,

}
