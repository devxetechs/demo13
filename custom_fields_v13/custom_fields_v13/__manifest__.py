# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyrig# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'custom fields in sale order',
    'version': '0.1',
    'category': 'sale',
    # 'sequence': 15,
    'summary': 'custom fields and mods',
    'description': """
        Custom fields 
    """,
    'author': 'Xetechs, S.A.',
    'website': 'https://www.xetechs.com',
    'depends': ['base_setup', 'sale'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}