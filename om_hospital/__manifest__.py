{
    'name': 'Hospital Management',
    'version': '1.o',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/kids_view.xml',
        'views/sale.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}