# -*- coding: utf-8 -*-
# © 2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super(AccountInvoiceLine, self)._onchange_product_id()
        for this in self:
            part = this.invoice_id.partner_id
            typeinv = self.invoice_id.type
            if this.product_id:
                if part and part.lang:
                    product = this.product_id.with_context(lang=part.lang)
                else:
                    product = this.product_id
                if typeinv in ('in_invoice', 'in_refund'):
                    description = product.description_purchase
                else:
                    description = product.description_sale
                this.name = ' '.join(
                    [product.name or '', description or '']
                ).strip()
        return res
