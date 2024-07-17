from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    package = fields.Char(string="Package")
    sub_category = fields.Char(string="Sub Category")
    part_number = fields.Char(string="Part No")
    resistance = fields.Char(string="Resistance")
    power_rating = fields.Char(string="Power Rating")
    package = fields.Char(string="Package")
    sub_category = fields.Many2one('product.product', string="Sub Category")
    temp_coefficient = fields.Char(string="TEMP. COEFFICIENT")
    min_oper_temp = fields.Char(string="Minimum Operating Temperature")
    max_oper_temp = fields.Char(string="Maximum Operating Temperature")
    Value = fields.Char(string="Value")
    voltage_rating = fields.Char(string="Voltage Rating")
    remark = fields.Text(string="Remark")
    part_number = fields.Char(string="Part Number")
    tolerance = fields.Char(string="Tolerance")
    watts = fields.Char(string="WATTAGE")
    qty = fields.Char(string="Quentity")
    issued_qty = fields.Char(string="Issued Quantity")
    total_qty = fields.Char(string="Total Quantity")
    manufacturer = fields.Char(string="Manufacturer")
    supplier = fields.Char(string="Supplier")
    forward_voltage = fields.Char(string="Forward voltage")
    breakdown_voltage = fields.Char(string="Breakdown voltage")
    rev_voltage = fields.Char(string="Rev. Voltage")
    forward_current = fields.Char(string="Forward current")
    location = fields.Char(string="Location")
    hsn_code = fields.Integer(string="HSN Code")
    hsn_description = fields.Char(string="HSN Description")
    current_rating = fields.Char(string="Current rating")
    # power_dissipation = fields.Char(string="Power Dissipation")
    output_current = fields.Char(string="Output current")
    output_voltage = fields.Char(string="Output voltage")
    vol_type = fields.Char(string="Voltage Type")
    min_vlt = fields.Char(string="Minimun voltage")
    max_vlt = fields.Char(string="Maximum Voltage")
    load_capaci = fields.Char(string="Load capacitance")
    no_of_position = fields.Char(string="No.of position")
    pitch = fields.Char(string="Pitch")
    dsv = fields.Char(string="Drain to Source Voltage (Vdss)")
    vgs = fields.Char(string="VGS (max)")
    cc_m = fields.Char(string="Current - Collector (Ic) (Max)")

    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', ('part_number', operator, name), ('sub_category', operator, name)]
        return self.search(domain + args, limit=limit).name_get()
