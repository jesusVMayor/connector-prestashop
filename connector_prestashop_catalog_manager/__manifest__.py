# -*- coding: utf-8 -*-
# Copyright 2011-2013 Camptocamp
# Copyright 2011-2013 Akretion
# Copyright 2015 AvanzOSC
# Copyright 2015-2016 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Prestashop-Odoo Catalog Manager",
    "version": "9.0.1.0.2",
    "license": "AGPL-3",
    "depends": [
        "connector_prestashop"
    ],
    "author": "Akretion,"
              "AvanzOSC,"
              "Tecnativa,"
              'Camptocamp SA,'
              "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/connector-prestashop",
    "category": "Connector",
    "data": [
        'views/product_attribute_view.xml',
        'views/product_view.xml',
        'wizards/export_category_view.xml',
        'wizards/export_multiple_products_view.xml',
        'wizards/sync_products_view.xml',
        'wizards/active_deactive_products_view.xml',
        'views/product_image_view.xml',
    ],
    'installable': False,
}
