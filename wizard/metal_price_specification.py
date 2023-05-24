from odoo import api, fields, models
from datetime import date, datetime, timedelta
import calendar


class MetalPriceSpecification(models.TransientModel):
    _name = "metal.price.specification"
    _description = 'Metal Price Specification wizard'

    target_date = fields.Date(string="Date",default = lambda self: self._compute_date_from())
    price = fields.Float(string="Price", default=0.0)


    def save_record(self):
        # self.env['daily.metal.price'].create({
        #     'name': '',
        #     'date': '',
        #     'price':0.0
        # })

        return {
            'name': "List of daily metal prices",
            'view_mode': 'form',
            'view_id': self.env.ref('custom_invoicing_module.daily_metal_price_form_view')._origin.id,
            'res_model': 'custom_invoicing_module.daily.metal.price',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def _compute_date_from(self):
        return datetime.now().date().replace(month=1, day=1)