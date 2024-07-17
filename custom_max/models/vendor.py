from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(string=" Contact Name")
