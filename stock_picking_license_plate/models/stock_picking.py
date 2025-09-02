from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    license_plate = fields.Char(
        string='License Plate',
        help='Vehicle license plate for this transfer',
        tracking=True,
        size=20
    )

    driver_name = fields.Char(
        string='Driver Name',
        help='Name of the driver',
        tracking=True,
        size=100
    )

    driver_doc = fields.Char(
        string='Document of the Driver',
        help='Document ID of the driver (e.g., ID card, license)',
        tracking=True,
        size=100
    )

    carrier_name = fields.Char(
        string='Carrier Name',
        help='Name of the transport carrier',
        tracking=True,
        size=100
    )
    vat_number = fields.Char(
        string='CNPJ/CPF OR RUC',
        help='CNPJ/CPF for Brazil or RUC for Paraguay of the carrier',
        tracking=True,
        size=100
    )

    transport_notes = fields.Text(
        string='Transport Notes',
        help='Additional notes about the transport'
    )

    @api.model_create_multi
    def create(self, vals_list):
        # Formatear la placa antes de crear el registro
        for vals in vals_list:
            if 'license_plate' in vals and vals['license_plate']:
                vals['license_plate'] = vals['license_plate'].replace(' ', '').upper()
        return super().create(vals_list)

    def write(self, vals):
        # Formatear la placa antes de escribir
        if 'license_plate' in vals and vals['license_plate']:
            vals['license_plate'] = vals['license_plate'].replace(' ', '').upper()
        return super().write(vals)

    @api.constrains('license_plate')
    def _check_license_plate_format(self):
        """Validate license plate format if needed"""
        for record in self:
            if record.license_plate:
                # Solo validar, NO modificar aquí
                # Agregar validaciones adicionales si es necesario
                if len(record.license_plate) < 3:
                    raise ValidationError(_('License plate must be at least 3 characters long.'))

                # Validar que solo contenga caracteres alfanuméricos
                import re
                if not re.match(r'^[A-Z0-9]+$', record.license_plate):
                    raise ValidationError(_('License plate can only contain letters and numbers.'))

    def button_validate(self):
        """Override validate to check license plate requirement"""
        # Check if license plate is required for outgoing pickings
        require_license = self.env['ir.config_parameter'].sudo().get_param(
            'stock_license_plate.require_license_plate', default=False
        )

        if require_license and self.picking_type_code == 'outgoing' and not self.license_plate:
            raise ValidationError(_('License plate is required for delivery orders.'))

        return super().button_validate()
