from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _on_subtotal(self):
        for data in self:
            subtotal = 0
            for line in data.order_line:
                subtotal += line.price_subtotal
            data.on_subtotal = subtotal
            data._amount_all()

    def _on_subtotal_no_service(self):
        for data in self:
            subtotal = 0
            for line in data.order_line:
                if line.product_id.type != 'service':
                    subtotal += (line.product_id.standard_price * line.product_uom_qty)
            data.on_subtotal_no_service = subtotal
            data._amount_all()

    @api.depends("on_subtotal", "lpvv")
    def _on_mantenimiento_descuento(self):
        for data in self:
            if (data.lpvv == 'cif' or data.lpvv == 'fob') and data.pricelist_id.pricelist_type == 'estandar' and not data.mantenimientos_manuales:
                descuento = self.env['on.mantenimiento'].search(
                    [
                        ('rango_inferior', '<=', data.on_subtotal),
                        ('rango_superior', '>=', data.on_subtotal),
                        ('company_id', '=', data.company_id.id)
                    ]
                )
                data.on_mantenimiento_descuento = data.on_subtotal * (descuento[0].porcentaje_descuento/100)
            else:
                data.on_mantenimiento_descuento = 0
            data._amount_all()

    @api.depends("on_subtotal_no_service", "lpvv")
    def _on_mantenimiento_cif(self):
        for data in self:
            if data.lpvv == 'cif' and (data.pricelist_id.pricelist_type == 'estandar' or data.pricelist_id.pricelist_type == 'tier1' or data.pricelist_id.pricelist_type == 'tier2') and not data.mantenimientos_manuales:
                mantenimiento_cif = self.env['on.mantenimiento.cif'].search([('company_id', '=', data.company_id.id)])[0]
                data.on_mantenimiento_cif = data.on_subtotal_no_service * ((mantenimiento_cif.porcentaje_cif/100))
            else:
                data.on_mantenimiento_cif = 0
            data._amount_all()

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            if not order.mantenimientos_manuales:
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': amount_untaxed + amount_tax - order.on_mantenimiento_descuento + order.on_mantenimiento_cif,
                })
            else:
                amount_total = amount_untaxed + amount_tax
                if order.descuento_state:
                    amount_total -= order.manual_mantenimiento_descuento
                if order.mantenimiento_state:
                    amount_total += order.manual_mantenimiento_cif
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': amount_total,
                })
    @api.onchange('lpvv', 'pricelist_id')
    def update_data(self):
        for data in self:
            if data.id:
                data._on_subtotal_no_service()
                data.on_mantenimiento_descuento()
                data.on_mantenimiento_cif()
                data._amount_all()

    def _descuento_mantenimiento_state(self):
        for data in self:
            if (data.lpvv == 'cif' or data.lpvv == 'fob') and data.pricelist_id.pricelist_type == 'estandar' :
                data.descuento_state = True
            else:
                data.descuento_state = False

            if data.lpvv == 'cif' and (data.pricelist_id.pricelist_type == 'estandar' or data.pricelist_id.pricelist_type == 'tier1' or data.pricelist_id.pricelist_type == 'tier2') :
                data.mantenimiento_state = True
            else:
                data.mantenimiento_state = False

    lpvv = fields.Selection([('cif', 'CIF'), ('fob', 'FOB')], string="CIF / FOB")
    on_subtotal = fields.Monetary(compute="_on_subtotal", string='Subtotal')
    on_subtotal_no_service = fields.Monetary(compute="_on_subtotal_no_service")
    on_mantenimiento_descuento = fields.Monetary(compute="_on_mantenimiento_descuento", string="Descuento")
    on_mantenimiento_cif = fields.Monetary(compute="_on_mantenimiento_cif", string="Gastos CIF")
    mantenimientos_manuales = fields.Boolean(string="Mantenimientos manuales", default=False)
    manual_mantenimiento_descuento = fields.Monetary(string="Descuento")
    manual_mantenimiento_cif = fields.Monetary(string="Gastos CIF")
    descuento_state = fields.Boolean(compute="_descuento_mantenimiento_state")
    mantenimiento_state = fields.Boolean(compute="_descuento_mantenimiento_state")


SaleOrder()