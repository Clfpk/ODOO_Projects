from odoo import models, fields


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    #report_ids = fields.Many2many('custom_email_reports.report', string='Attached Reports')
    report_ids = fields.Many2many(
        'ir.actions.report', relation='mail_template_ir_actions_report_rel',
        column1='mail_template_id',
        column2='ir_actions_report_id',
        string='Attach Reports',
        domain="[('models', '=', models)]")

    def attach_reports(self, record_ids):

        for template in self:
            attachments = []
            for report in template.report_ids:
                report_obj = self.env['ir.actions.report'].search([('report_name', '=', report.report_name)])
                for record_id in record_ids:
                    report_data = report_obj.render_qweb_pdf(record_id)
                    attachments.append(('Report_%s.pdf' % report.report_name, report_data))

            attachment_values = []
            for attach in attachments:
                import base64
                attachment_values.append({
                    'name': attach[0],
                    'datas': base64.encodebytes(attach[1]),
                    'datas_fname': attach[0],
                })
            attachment_ids = [(0, 0, attachment) for attachment in attachment_values]

            template.attachment_ids = attachment_ids