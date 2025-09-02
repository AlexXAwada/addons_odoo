from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Campos existentes
    license_plate = fields.Char(string='License Plate')
    driver_name = fields.Char(string='Driver Name')
    driver_doc = fields.Char(string='Document of the Driver')
    carrier_name = fields.Char(string='Carrier Name')
    vat_number = fields.Char(string='VAT Number')
    transport_notes = fields.Text(string='Transport Notes')

    # Nuevo campo para el contacto transportadora
    carrier_partner_id = fields.Many2one(
        'res.partner',
        string='Carrier Partner',
        domain="[('is_carrier', '=', True)]",
        help='Select a partner with Carrier classification'
    )

    @api.onchange('carrier_partner_id')
    def _onchange_carrier_partner_id(self):
        """Auto-fill carrier info when partner is selected"""
        if self.carrier_partner_id:
            self.carrier_name = self.carrier_partner_id.name
            # Usar el VAT del partner, o si no tiene, usar el campo de identificación
            self.vat_number = self.carrier_partner_id.vat or ''
            if not self.vat_number and hasattr(self.carrier_partner_id, 'l10n_latam_identification_type_id'):
                identification = self.carrier_partner_id.l10n_latam_identification_type_id
                if identification:
                    self.vat_number = identification.name
        else:
            # Limpiar campos si se deselecciona el partner
            self.carrier_name = False
            self.vat_number = False

    @api.model
    def create(self, vals):
        """Override create to ensure carrier info is saved"""
        if 'carrier_partner_id' in vals and vals['carrier_partner_id']:
            partner = self.env['res.partner'].browse(vals['carrier_partner_id'])
            if partner:
                if not vals.get('carrier_name'):
                    vals['carrier_name'] = partner.name
                if not vals.get('vat_number'):
                    vals['vat_number'] = partner.vat or ''
        return super().create(vals)

    def write(self, vals):
        """Override write to ensure carrier info is updated"""
        if 'carrier_partner_id' in vals:
            if vals['carrier_partner_id']:
                partner = self.env['res.partner'].browse(vals['carrier_partner_id'])
                if partner:
                    vals['carrier_name'] = partner.name
                    vals['vat_number'] = partner.vat or ''
            else:
                vals['carrier_name'] = False
                vals['vat_number'] = False
        return super().write(vals)
