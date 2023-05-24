from odoo import fields, models, api
class Partner(models.Model):
    """
    Extensions of partner to add Algerian locale fields on a company.
    """
    _inherit = 'res.partner'

    total_quantity = fields.Float(strig="Total quantity", compute='_compute_field', store=True)

    #@api.depends('field1', 'field2')
    def _compute_field(self):
        for record in self:
            # domain = []
            # record.total_quantity= sum([r.total for r in self.env['account.move'].search(domain)])
            record.total_quantity = 0.0

    def action_view_partner_filtered_invoices(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("account.action_move_out_invoice_type")
        all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        # I should  adjust domain here
        action['domain'] = [
            ('move_type', 'in', ('out_invoice', 'out_refund')),
            ('partner_id', 'in', all_child.ids)
        ]
        action['context'] = {'default_move_type': 'out_invoice', 'move_type': 'out_invoice', 'journal_type': 'sale', 'search_default_unpaid': 1}
        return action