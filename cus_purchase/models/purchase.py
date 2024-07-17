from odoo import models, api, exceptions

class CustomInvoice(models.Model):
    _inherit = 'account.move'

    def post_invoice(self, invoice_ids):
        invoices = self.browse(invoice_ids)

        for invoice in invoices:
            if invoice.state != 'Posted':
                raise exceptions.UserError('Invoice is not posted.')
            invoice.action_post()



# from odoo import models, api
#
#
# class CustomInvoice(models.Model):
#     _inherit = 'account.move'
#     #
    # def post_invoice(self, invoice_id):
    #     invoice = self.browse(invoice_id)
    #
    #     if invoice.state != 'Posted':
    #         raise exceptions.UserError('Invoice is Posted.')
    #
    #     invoice.action_post()

#
# def post_invoice(self, invoice_id):
#     invoice = self.browse(invoice_id)
#
#     if invoice.state != 'Posted':
#         self.set_status('Invoice is not posted.')
#         return
#
#     invoice.action_post()
#     self.set_status('Invoice posted successfully.')
#
#     invoice.action_post()

# #
# # def post_invoice(self):
# #     for move in self:
# #         if move.custom_posted_status == 'posted':
# #             raise UserError('This invoice is already posted.')
# #
# #         # Call the super method to perform the standard post operation
# #         res = super(AccountMove, self).post()
# #     #
# #     #     # Update the custom posted status
# #     #     move.custom_posted_status = 'posted'
# #     # return res
#
# def post_invoice(self, invoice_id):
#     invoice = self.browse(invoice_id)
#
#     if invoice.state != 'Posted':
#         raise exceptions.UserError('Invoice is Posted.')
#
#     invoice.action_post()
