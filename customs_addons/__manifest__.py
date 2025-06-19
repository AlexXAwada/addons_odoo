{
    "name": "Regulatorio de Logística",
    "author": "FFA",
    "version": "15.0.0.1",
    "category": "Inventory/Logistics",
    "summary": "Módulo para agregar la funcionalidad de regulatorio de logística",
    "description": """
Este módulo agrega funcionalidad de regulatorio de logística a los productos,
incluyendo campos de fecha de inicio para control de inventario.

Características:
- Campo de fecha de inicio en productos
- Vistas mejoradas para gestión logística
    """,
    "depends": ["product"],
    "data": [
        "views/registro_logistica.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "LGPL-3",
}
