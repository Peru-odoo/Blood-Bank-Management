from odoo import fields, models

class inventoryBlood(models.Model):
    _name = "inventory.blood"
    _description = "Inventory Blood"

    blood_group = fields.Selection(
        string="Blood Group Needed",
        selection=[
            ('a_pos', 'A+'),
            ('a_neg', 'A-'),
            ('b_pos', 'B+'),
            ('b_neg', 'B-'),
            ('ab_pos', 'AB+'),
            ('ab_neg', 'AB-'),
            ('o_pos', 'O+'),
            ('o_neg', 'O-'),
        ],
        required=True,
    )
    quantity_inventory = fields.Float(string="Quantity (l)", required=True, default=0)
    expiry = fields.Date(string='Expiry Date', required=True)
    location = fields.Char(string='Location')
