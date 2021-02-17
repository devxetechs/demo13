from odoo import _, api, fields, models


class OnMantenimiento(models.Model):
    _name = 'on.mantenimiento'

    rango_inferior = fields.Float(string='Rango inferior')
    rango_superior = fields.Float(string='Rango superior')
    porcentaje_descuento = fields.Float(string='Porcentaje de descuento')
    company_id = fields.Many2one('res.company', string='Compañia')