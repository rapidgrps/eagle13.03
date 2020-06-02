# -*- encoding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.
{
    'name': 'Fleet History',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Get history of driven cars by employees',
    'description': "",
    'depends': ['hr', 'fleet'],
    'data': [
        'views/employee_views.xml',
        'views/fleet_vehicle_views.xml',
    ],
    'auto_install': True,
}
