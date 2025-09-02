from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    classification_ids = fields.Many2many(
        'contact.classification',
        'partner_classification_rel',
        'partner_id',
        'classification_id',
        string='Classifications',
        help='Select one or more classifications for this contact'
    )

    # Campos computed para facilitar filtros y reportes
    is_client = fields.Boolean(
        string='Is Client',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Client'
    )

    is_supplier = fields.Boolean(
        string='Is Supplier',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Supplier'
    )

    is_director = fields.Boolean(
        string='Is Director',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Director'
    )

    is_employee = fields.Boolean(
        string='Is Employee',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Employee'
    )

    is_salesperson = fields.Boolean(
        string='Is Salesperson',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Salesperson'
    )

    is_carrier = fields.Boolean(
        string='Is Carrier',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Carrier'
    )

    is_bank = fields.Boolean(
        string='Is Bank',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Bank'
    )

    is_other = fields.Boolean(
        string='Is Other',
        compute='_compute_classification_booleans',
        store=True,
        help='Contact is classified as Other'
    )

    classification_display = fields.Char(
        string='Classifications',
        compute='_compute_classification_display',
        help='Display all classifications as text'
    )

    @api.depends('classification_ids')
    def _compute_classification_booleans(self):
        for partner in self:
            codes = partner.classification_ids.mapped('code')
            partner.is_client = 'client' in codes
            partner.is_supplier = 'supplier' in codes
            partner.is_director = 'director' in codes
            partner.is_employee = 'employee' in codes
            partner.is_salesperson = 'salesperson' in codes
            partner.is_carrier = 'carrier' in codes
            partner.is_bank = 'bank' in codes
            partner.is_other = 'other' in codes

    @api.depends('classification_ids')
    def _compute_classification_display(self):
        for partner in self:
            if partner.classification_ids:
                partner.classification_display = ', '.join(
                    partner.classification_ids.mapped('name')
                )
            else:
                partner.classification_display = ''

    def action_add_classification(self):
        """Action to add classifications"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Classifications',
            'res_model': 'contact.classification.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_partner_ids': [(6, 0, self.ids)]},
        }
