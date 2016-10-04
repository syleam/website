# -*- coding: utf-8 -*-
##############################################################################
#
#    website_sale_products_sorted module for OpenERP, Module
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Yannis Pou-Vich <yannis.pouvich@syleam.fr>
#
#    This file is a part of website_sale_products_sorted
#
#    website_sale_products_sorted is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    website_sale_products_sorted is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class WebsiteAdminProductsSortedLine(models.Model):
    _name = 'website.admin.products.sorted.line'
    _description = 'Website Admin Products Sorted Line'

    website_id = fields.Many2one(comodel_name='website', string='website', required=True)
    sequence = fields.Integer(string='Sequence', help='Define order of list in field select')
    field_product_id = fields.Many2one(comodel_name='ir.model.fields', string='Field Product', domain=[('model_id.model', '=', 'product.template')], help='Field of product to sort products')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
