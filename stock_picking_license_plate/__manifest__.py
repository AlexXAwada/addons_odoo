{
    'name': 'Stock Picking License Plate',
    'version': '15.0.1.0.0',
    'category': 'Inventory',
    'depends': ['base','stock'],
    'author': 'FFA-DEV, Alexandre Awada',
    'license': 'AGPL-3',
    'summary': 'License plate and name of the carrier on stock picking',
    'description': '''
        This module adds license plate field to stock picking operations.
        Allows to track vehicle license plates in inventory transfers.
    ''',
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views_simple.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
