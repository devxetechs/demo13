from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_admin = fields.Boolean('is admin', compute='_is_admin')

    @api.depends('product_id')
    def _is_admin(self):
        self.update({'is_admin': self.env.user.has_group('base.group_system')})