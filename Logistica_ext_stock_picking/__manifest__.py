{
    'name': 'Logística - Extensión de Stock Picking',
    'version': '15.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Agregar campos de logística a las transferencias de stock',
    'description': """
        Extensión del módulo de stock para agregar información logística:
        - Vía de transporte (terrestre, aéreo, multimodal, marítimo, fluvial)
        - Fechas ETD, ETA Transbordo, ETA Aduana
        - Información de contenedor/chapa
        - Número de embarque
        - Estado logístico (pendiente/hecho)
    """,
    'author': 'FFA-DEV, Alexandre Awada',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
