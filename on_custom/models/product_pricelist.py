from odoo import _, api, fields, models


class ProductPriceList(models.Model):
    _inherit = 'product.pricelist'

    pricelist_type = fields.Selection([('estandar', 'Estandar'), ('tier1', 'Tier 1'), ('tier2', 'Tier 2')], string="Tipo de tarifas")