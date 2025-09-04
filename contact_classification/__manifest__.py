{
    'name': 'Contact Classification',
    'version': '15.0.1.0.0',
    'summary': 'Clasificación avanzada de contactos',
    'description': """
        Módulo para clasificar contactos con múltiples categorías:
        - Cliente
        - Proveedor
        - Director
        - Funcionario
        - Vendedor
        - Transportadora
        - Banco
        - Otros
    """,
    'author': 'FFA-DEV, Alexandre Awada',
    'category': 'Contacts',
    'depends': ['base', 'contacts'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/contact_classification_data.xml',
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
