# See LICENSE file for full copyright and licensing details.
{
    "name": "Transport Management System",
    "version": "Beta",
    "author": "EZZIOURI Oussama",
    "website": "http://www.leoni.com",
    "category": "Transport",
    "sequence": 1,
    "license": "AGPL-3",
    "complexity": "easy",
    "summary": "Transport Management System for inbound and outbound flow",
    "description": "The Transport Management System module in Odoo provides a comprehensive solution to optimize transportation operations. Manage your fleet, plan routes, track shipments, and monitor costs. Seamlessly integrate with other Odoo modules for enhanced efficiency and control.",
    "images": ["static/icon.png"],
    "depends": ["base", "purchase"],
    "data": [
        'views/tp_menus.xml',
        'views/tp_truck_views.xml',
        'views/tp_departure_views.xml',
        'views/tp_fdp_views.xml',
#        'security/tp_security.xml',
        'security/ir.model.access.csv',
    ],
    "assets": {},
    "installable": True,
    "application": True
}
