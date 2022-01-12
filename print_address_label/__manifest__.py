# -*- coding: utf-8 -*-
{
    'name': "Print Address Label",

    'summary': """Allows to print address labels as pdf""",

    'description': """
        Allows to print address labels as pdf
    """,

    'author': "Abilium GmbH",
    'website': "https://www.abilium.io",

    'category': 'Hidden',
    'version': '1.0',
    'auto_install': False,

    'depends': [
        'base'
    ],

    'data': [
        'reports/paperformat_address_label.xml',
        'reports/address_label.xml'
    ]
}
