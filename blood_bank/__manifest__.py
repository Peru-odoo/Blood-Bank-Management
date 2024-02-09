{
    'name': "blood bank",
    'version': '1.0',
    'depends': ['base'],
    'data':
        [
         'security/ir.model.access.csv',
         'views/donor_views.xml',
         'views/donation_views.xml',
         'views/inventory_views.xml',
         'views/request_views.xml',
         'views/transfusion_views.xml',
         'views/blood_bank_menus.xml',
        ],
    'author': "nihp-blood-bank",
    'application': True,
    'installable': True,
    'liscense': 'LGPL-3',
}
