{
    'name': 'MySchool',
    'version': '15.0',
    'summary': 'MySchool',
    'sequence': 10,
    'description': """""",
    'category': 'Sales/Sales',
    'website': '',
    'depends': [
        'mail'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/class.xml',
        'views/section.xml',
        'report/report.xml',
        'report/student_card.xml',


    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}