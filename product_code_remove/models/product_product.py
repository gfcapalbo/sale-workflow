# -*- coding: utf-8 -*-
# © 2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api,  models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def name_get(self):
        res = []
        for this in self:
            return_val = super(ProductProduct, self).name_get()
            res.append((this.id, (this.name)))
        return res or return_val
