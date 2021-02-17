from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_admin = fields.Boolean('is admin', compute='_is_admin')

    @api.depends('product_id')
    def _is_admin(self):
        self.update({'is_admin': self.env.user.has_group('base.group_system')})


class CrmLead(models.Model):
	_inherit = 'crm.lead'

	oportunity_mw = fields.Float('Oportunity MV', readonly=False, digits=(12,3))
	project_amount = fields.Float('Project Amount', readonly=False, digits=(12,2))	
