{
    'name': 'Hospital Management',
    'version': '1.o',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}