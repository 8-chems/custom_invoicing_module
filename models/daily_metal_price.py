
from odoo import models, fields

class DailyMetalPrice(models.Model):
    _name = "daily.metal.price"
    _description = "This model contains customization of the partner model to satisfy recruiter requirements."

    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", required=True, default=0.0, help="")
    target_date = fields.Date(string='Date')

