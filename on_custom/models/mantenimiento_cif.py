from odoo import _, api, fields, models


class OnMantenimientoCif(models.Model):
    _name = 'on.mantenimiento.cif'

    porcentaje_cif = fields.Float(string='% CIF')
    company_id = fields.Many2one('res.company', string='Compañia')
