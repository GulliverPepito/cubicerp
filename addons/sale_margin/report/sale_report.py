# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE_LGPL file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin = fields.Float('Margin')

    def _select(self):
        return super(SaleReport, self)._select() + ", SUM(l.margin / COALESCE(cr.rate, 1.0)) AS margin"
