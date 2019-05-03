# -*- coding: utf-8 -*-
# Copyright 2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api,  models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def name_get(self):
        for this in self:
            res = super(ProductProduct, this).name_get()
            return_val_split = res[0][1].split()
            for element in return_val_split:
                possible_codes = [this.default_code]
                # TODO If needed add supplier codes to possible codes
                for possible_code in possible_codes:
                    if element == "[%s]" % possible_code:
                        return_val_split.remove(element)
                return_val = ' '.join(return_val_split)
                res = [(x[0], return_val) for x in res]
            return res
