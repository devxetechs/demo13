from odoo import api, fields, models, _



class ResCompany(models.Model):
    _inherit = 'res.company'

    cybersource_merchant_id = fields.Char('Merchant id Cybersource', default="dummy")
    cybersource_org_id = fields.Selection([('1snn5n9w', 'Prod Enviroment'), ('1snn5n9w', 'Test Enviroment')], string="Org ID")

