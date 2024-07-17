from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_limit = fields.Monetary(string='Invoice Limit', default=10000.0, help="Set the maximum limit for invoice amounts")

    @api.model
    def create(self, vals):
        if 'amount_total' in vals and vals['amount_total'] > self.env.user.company_id.invoice_limit:
            raise ValidationError("The invoice amount exceeds the allowed limit of %s" % self.env.user.company_id.invoice_limit)
        return super(AccountMove, self).create(vals)

    def write(self, vals):
        if 'amount_total' in vals and vals['amount_total'] > self.env.user.company_id.invoice_limit:
            raise ValidationError("The invoice amount exceeds the allowed limit of %s" % self.env.user.company_id.invoice_limit)
        return super(AccountMove, self).write(vals)

    @api.onchange('invoice_line_ids')
    def _onchange_invoice_line_ids(self):
        if self.amount_total > self.invoice_limit:
            raise ValidationError("The invoice amount exceeds the allowed limit of %s" % self.invoice_limit)


# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
#
# class AccountMove(models.Model):
#     _inherit = 'account.move'
#
#     invoice_limit = fields.Monetary(string='Invoice Limit', default=10000.0, help="Set the maximum limit for invoice amounts")
#
#     def action_post(self):
#         for record in self:
#             if record.amount_total > record.invoice_limit:
#                 raise ValidationError("The invoice amount exceeds the allowed limit of %s" % record.invoice_limit)
#         super(AccountMove, self).action_post()
