# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# @author Alexis de Lattre <alexis.delattre@akretion.com>

{
    'name': 'Sale Order Report ',
    'version': '13.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Adds fields to the report of Sale Order',
    'description': """
Sale Order Report
====================
    """,
    'author': 'Xetechs',
    'maintainer': 'Juan Carlos Ortega',
    'website': 'http://www.xetechs.com',
    'depends': ['sale'],
    'data': ['views/sale_order_report.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
