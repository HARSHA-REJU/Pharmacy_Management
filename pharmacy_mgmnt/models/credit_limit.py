from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api, tools

from openerp.exceptions import Warning
from openerp.tools.translate import _



class CreditLimitCustomer(models.Model):
    _inherit = 'res.partner'

    @api.one
    @api.depends('limit_amt', 'used_credit_amt')
    def _compute_credited_amt(self):
        credit_ltd = self.limit_amt
        cust_obj = self.env['account.invoice'].search([('partner_id', '=', self.name)])
        if cust_obj:
            sum = 0
            for item in cust_obj:
                if item.state == 'paid':
                    if item.pay_mode == 'credit':
                        if item.partner_id.id == self.id:
                            sum = sum + item.amount_total
                            print(item.partner_id.id)
                            print(self.name)
            print("used amount", sum)
            self.used_credit_amt = sum

    limit_amt = fields.Float('Credit Limit Amount')
    used_credit_amt = fields.Float('Used Amount', compute="_compute_credited_amt")
