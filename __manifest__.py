# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CustomInvoicing',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
        This module is developed under Odoo 16.
        It is developed to satisfy recruiter assessment specifications.
        """,
    'depends': ['base', 'account'],
    'auto_install': True,
    'data': [
        'security/ir.model.access.csv',
        'views/daily_metal_price.xml',
        'views/custom_invoicing.xml',
        # 'views/account_move_line.xml',
        'wizard/metal_price_specification_wizard_view.xml',
        'views/menu_items.xml',
        'views/res_partner.xml',

    ],
    'qweb': [],
    'bootstrap': True,  # load translations for login screen
}
