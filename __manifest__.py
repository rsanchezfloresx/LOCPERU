# -*- coding: utf-8 -*-
{
    'name': "Localizacion Peru FE",

    'summary': """
        Facturacion Electronica
        PERU""",

    'description': """
        Facturacion Electronica automatica
    """,

    'author': "GBS",
    'website': "http://www.gbs.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'LocPeru',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/fe.xml',
        'views/fe_import.xml',
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
