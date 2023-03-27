from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api, tools

from openerp.exceptions import Warning
from openerp.tools.translate import _



class CreditLimitCustomer(models.Model):
    _inherit = 'res.partner'


    def _compute_credited_amt(self):
        for rec in self:
            customer_invoices = rec.env['account.invoice'].search([('pay_mode','=','credit'),
                                                           ('partner_id', '=', rec.id),
                                                           ('type','=', 'out_invoice'),
                                                           ('state','=','open')])
            rec.used_credit_amt = sum(customer_invoices.mapped('amount_total'))

    limit_amt = fields.Float('Credit Limit Amount')
    used_credit_amt = fields.Float('Used Amount', compute="_compute_credited_amt")
