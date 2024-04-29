# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hangry HR Management',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 240,
    'summary': 'Track employee Hangry',
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    'website': 'https://www.odoo.com/app/employees',
    'depends': ['base', 'hr', 'hr_attendance'],
    'data': [
        'security/hangry_hr_security.xml',
        'security/ir.model.access.csv',
        'wizard/wiz_employee_user_views.xml',
        'views/hr_attendance_views.xml',
        'views/hr_employee_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'assets': {
    },
    'license': 'LGPL-3',
}
