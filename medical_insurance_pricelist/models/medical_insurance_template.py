# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalInsuranceTemplate(models.Model):
    _inherit = 'medical.insurance.template'
    pricelist_id = fields.Many2one(
        string='Pricelist',
        comodel_name='product.pricelist',
        help='Pricelist for plan',
    )
