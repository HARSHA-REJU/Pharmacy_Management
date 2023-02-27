from datetime import datetime, timedelta
from datetime import timedelta
import openerp.addons.decimal_precision as dp
from openerp.exceptions import except_orm, Warning, RedirectWarning


# import models
from dateutil.relativedelta import relativedelta

from openerp import models, fields, api, tools, _


class ChequeTransactions(models.Model):
    _name = 'cheque.entry'
    _rec_name = 's_no'

    s_no = fields.Char('Serial Number', readonly=True, required=True, copy=False, default='New')
    name = fields.Many2one('res.partner', 'Name', required=1)
    t_date = fields.Date('Date', required=1)
    cheque_no = fields.Char('Cheque Number')
    cheque_date = fields.Date('Cheque Date')
    deposit_date = fields.Date('Deposit Date')
    clearance_date = fields.Date('Clearance Date')
    cheque_amount = fields.Float('Cheque Amount', required=1)
    balance = fields.Float('Balance', compute="_get_balace_amt")
    bank = fields.Char('Bank')
    branch = fields.Char('Branch')
    ifsc = fields.Char('IFSC')
    state = fields.Selection([('draft', 'Draft'), ('post', 'Posted'), ('bounce', 'Bounced'), ]
                             , required=True, default='draft')
    invoice_ids = fields.Many2many('account.invoice', string="Select Invoice")

    @api.one
    @api.depends('cheque_amount')
    def _get_balace_amt(self):
        if self.state == 'post':
            self.balance = self.cheque_amount
        if self.state == 'bounce':
            self.balance = 0.0

    @api.model
    def create(self, vals):
        if vals.get('s_no', 'New') == 'New':
            vals['s_no'] = self.env['ir.sequence'].next_by_code(
                'cheque.entry.sequence') or 'New'
        result = super(ChequeTransactions, self).create(vals)
        return result

    @api.multi
    def post(self):
        for rec in self:
            rec.write({'state': 'post'})
            if rec.balance == 0:
                rec.balance = self.cheque_amount
            if rec.invoice_ids:
                new_debit = 0
                for item in rec.invoice_ids:
                    if item.state != 'paid':
                        new_debit = item.account_id.debit - item.amount_total
                        item.account_id.write({'debit': new_debit})
                        # print("99999999999999999999999999999999999",new_debit)
                        item.paid_bool = True
                        item.write({'state': 'paid'})

    @api.multi
    def bounce(self):
        for rec in self:
            rec.balance = 0
            rec.write({'state': 'bounce'})




