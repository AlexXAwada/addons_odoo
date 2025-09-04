# models/stock_picking.py
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Campo para la vía de transporte
    via_transporte = fields.Selection([
        ('terrestre', 'Terrestre'),
        ('aereo', 'Aéreo'),
        ('multimodal', 'Multimodal'),
        ('maritimo', 'Marítimo'),
        ('fluvial', 'Fluvial'),
    ], string='Vía de Transporte')

    # Campos de fecha
    etd_fecha = fields.Datetime(string='ETD (Estimated Time of Departure)')
    eta_transbordo_fecha = fields.Datetime(string='ETA Transbordo')
    eta_aduana_fecha = fields.Datetime(string='ETA Aduana')

    # Campo para contenedor o chapa
    contenedor_chapa = fields.Char(string='Contenedor/Chapa')

    # Campo para número de embarque
    numero_embarque = fields.Char(string='Número de Embarque')

    # Campo de estado logístico
    estado_logistico = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('hecho', 'Hecho'),
    ], string='Estado Logístico', default='pendiente')

    # Campo para notas logísticas
    notas_logisticas = fields.Text(string='Notas Logísticas')
