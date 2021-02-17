{
    'name': 'Custom account move',
    'version': '0.1',
    'category': 'sale',
    'summary': 'Formulas y procesos a Requerimiento: Listas de Precio Ventas Por volumen CIF/FOB Cliente Estándar y Listas de Precio CIF/FOB Partner T1/T2					',
    'description': """
        Formulas y procesos a Requerimiento: Listas de Precio Ventas Por volumen CIF/FOB Cliente Estándar y Listas de Precio CIF/FOB Partner T1/T2					
    """,
    'author': 'Xetechs, S.A.',
    'website': 'https://www.xetechs.com',
    'depends': ['base', 'base_setup', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menu.xml',
        'views/sale_order.xml',
        'views/product_pricelist.xml',
        'views/account_move.xml',
        'reports/sale_order.xml',
        'reports/account_move.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
