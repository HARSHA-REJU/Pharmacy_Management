from openerp import models, fields, api, _
from openerp import tools, _
from datetime import datetime, date, timedelta


class CustomerInvoiceReport(models.TransientModel):
    _name = 'purchase.invoice.report'

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')
    product = fields.Many2one('product.product', 'Product')
    group = fields.Many2one('tax.combo.new', 'Group')
    potency = fields.Many2one('product.medicine.subcat', 'Potency')
    packing = fields.Many2one('product.medicine.packing', 'Packing')
    company = fields.Many2one('product.medicine.responsible', 'Company')

    @api.multi
    def action_purchase_report_open_window(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }

        return {
            'name': 'Purchase Report',
            'type': 'ir.actions.report.xml',
            'report_name': 'pharmacy_mgmnt.purchase_report_template_new',
            'datas': datas,
            'report_type': 'qweb-pdf'
        }

    @api.multi
    def view_purchase_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'pharmacy_mgmnt.purchase_report_template_new',
            'datas': datas,
            'report_type': 'qweb-html',
        }

    @api.multi
    def get_details(self):
        lst=[]
        if self.date_from:
            cust_invs = self.env['account.invoice'].search(
                [('date_invoice', '>=', self.date_from), ('date_invoice', '<=', self.date_to),
                 ])
            for rec in cust_invs:
                if rec.state == 'draft':
                    pass
                else:
                    for lines in rec.invoice_line:
                        if self.product.id and self.company.id and self.group.id and self.packing.id and self.potency.id:
                            if ((lines.product_id.id == self.product.id) and (
                                            lines.product_of.id == self.company.id)
                                    and (lines.medicine_grp.id == self.group.id) and (
                                            lines.medicine_name_packing.id == self.packing.id) and (lines.medicine_name_subcat.id == self.potency.id)):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.product.id and self.company.id and self.group.id and self.packing.id:
                        if ((lines.product_id.id == self.product.id) and (
                                lines.product_of.id == self.company.id)
                                and (lines.medicine_grp.id == self.group.id) and (
                                        lines.medicine_name_packing.id == self.packing.id)):
                            if (self.potency.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.product.id and self.company.id and self.group.id and self.potency.id:
                        if ((lines.product_id.id == self.product.id) and (
                                lines.product_of.id == self.company.id)
                                and (lines.medicine_grp.id == self.group.id)and (
                                        lines.medicine_name_subcat.id == self.potency.id)):
                            if (self.packing.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.product.id and self.company.id and self.packing.id and self.potency.id:
                        if ((lines.product_id.id == self.product.id) and (
                                lines.product_of.id == self.company.id)
                                and (lines.medicine_name_packing.id == self.packing.id)and (
                                        lines.medicine_name_subcat.id == self.potency.id)):
                            if (self.group.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.company.id and self.group.id and self.potency.id:
                        if ((lines.product_of.id == self.company.id)
                                and (lines.medicine_grp.id == self.group.id)and (
                                        lines.medicine_name_subcat.id == self.potency.id)):
                            if (self.packing.id == False) and (self.product.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.company.id and self.group.id and self.product.id:
                        if ((lines.product_id.id == self.product.id)
                                and (lines.medicine_grp.id == self.group.id)and (
                                        lines.product_of == self.company.id)):
                            if (self.packing.id == False) and (self.potency.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.company.id and self.group.id and self.product.id and self.potency.id:
                        if ((lines.product_id.id == self.product.id)
                                and (lines.medicine_grp.id == self.group.id)and (
                                        lines.product_of == self.company.id)):
                            if (self.packing.id == False) and (self.potency.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.company.id and self.group.id:
                        if ((lines.medicine_grp.id == self.group.id) and (
                                        lines.product_of == self.company.id)):
                            if (self.packing.id == False) and (self.potency.id == False) and (self.product.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)
                    if self.company.id and self.potency.id:
                        if ((lines.medicine_name_subcat.id == self.potency.id) and (
                                        lines.product_of == self.company.id)):
                            if (self.packing.id == False) and (self.group.id == False) and (self.product.id == False):
                                vals = {
                                    'inv_no': rec.number,
                                    'product': lines.product_id.name,
                                    'batch': lines.batch_2.batch,
                                    'expiry': lines.expiry_date,
                                    'rack': lines.medicine_rack.medicine_type,
                                    'qty': round(lines.quantity, 0),
                                }
                                lst.append(vals)

        return lst
