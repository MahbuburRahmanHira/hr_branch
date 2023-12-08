# -*- coding: utf-8 -*-
{
    'name': 'HR Branch',
    'version': '16.0.1.0.0',
    'description': 'This module is designed based on NGO branches.',
    'author': 'Mahbubur Rahman Hira',
    'website': 'https://www.youtube.com/@OdooLearning',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'hr'

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/branch_views.xml',
        'views/region_views.xml',
        'views/zone_views.xml',
        'views/area_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'BDT',
    'license': 'OPL-1',

}
