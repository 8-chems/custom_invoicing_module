
from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'Account Move'


    today_metal_price = fields.Many2one("daily.metal.price",string='Metal Price'
                                        , change_default=True,
                                          default= lambda self: self._default_computed_field())


    def _default_computed_field(self):
        return None