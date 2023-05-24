



from odoo import fields, models, api, exceptions

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = 'Account Move'

    # price_subtotal = fields.Monetary(
    #     string='Subtotal',
    #     compute='_compute_totals', store=True,
    #     currency_field='currency_id',
    # )
    # price_total = fields.Monetary(
    #     string='Total',
    #     compute='_compute_totals', store=True,
    #     currency_field='currency_id',
    # )
    #
    # @api.depends('quantity', 'discount', 'price_unit', 'tax_ids', 'currency_id')
    # def _compute_totals(self):
    #     for line in self:
    #         if line.display_type != 'product':
    #             line.price_total = line.price_subtotal = False
    #         # Compute 'price_subtotal'.
    #         line_discount_price_unit = line.price_unit * (1 - (line.discount / 100.0))
    #         subtotal = line.quantity * line_discount_price_unit
    #
    #         # Compute 'price_total'.
    #         if line.tax_ids:
    #             taxes_res = line.tax_ids.compute_all(
    #                 line_discount_price_unit,
    #                 quantity=line.quantity,
    #                 currency=line.currency_id,
    #                 product=line.product_id,
    #                 partner=line.partner_id,
    #                 is_refund=line.is_refund,
    #             )
    #             line.price_subtotal = taxes_res['total_excluded']
    #             line.price_total = taxes_res['total_included']
    #         else:
    #             line.price_total = line.price_subtotal = subtotal

    @api.onchange('price_total')
    def _on_price_total_change(self):
        # Perform actions when field_name changes
        # Access the field value using self.field_name

        if self.price_total:
            # Call a method or perform specific actions
            self._adjust_calculation()

    def _adjust_calculation(self):
        # Custom method implementation
        pass

    @api.onchange('total')
    def _on_total_change(self):
        if self.total and not self.quantity:
            raise exceptions.UserError('Quantity should be required when Total is entered.')