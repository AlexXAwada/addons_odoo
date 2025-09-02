from odoo import models, fields, api

class ContactClassification(models.Model):
    _name = 'contact.classification'
    _description = 'Contact Classification'
    _order = 'sequence, name'

    name = fields.Char(
        string='Classification Name',
        required=True,
        translate=True
    )

    code = fields.Char(
        string='Code',
        required=True,
        help='Unique code for this classification'
    )

    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help='Used to order classifications'
    )

    color = fields.Integer(
        string='Color',
        help='Color for kanban view'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    description = fields.Text(
        string='Description',
        translate=True
    )

    partner_count = fields.Integer(
        string='Partner Count',
        compute='_compute_partner_count'
    )

    @api.depends()
    def _compute_partner_count(self):
        for record in self:
            record.partner_count = self.env['res.partner'].search_count([
                ('classification_ids', 'in', record.id)
            ])

    def action_view_partners(self):
        """Action to view partners with this classification"""
        return {
            'type': 'ir.actions.act_window',
            'name': f'Partners - {self.name}',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('classification_ids', 'in', self.id)],
            'context': {'default_classification_ids': [(4, self.id)]},
        }

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'The code must be unique!'),
    ]
