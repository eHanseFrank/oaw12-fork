# -*- coding: utf-8 -*-
from openerp import models, fields, api



class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_ref_report = fields.Char(
        string="Code",
        store=True,
    )

    quot_report_note = fields.Text(
        'Notes'
    )
    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        # For quotation adjust: set new order_ref field
        if 'name' in vals and 'partner_id' in vals:
              name = vals['name']
              #Get the reference number number
              fragments_order_ref = vals['name'].split("-")
              sub_order_ref = fragments_order_ref[-1]
              #Get the partner id
              domain = [
                  ('id', '=', vals['partner_id']),
              ]
              partner_id = self.env['res.partner'].search(domain)
              partner_ref = partner_id.ref
              # New reference
              if partner_ref == False:
                  partner_ref = partner_id.name
              res.order_ref_report = sub_order_ref+" "+partner_ref
        return res


