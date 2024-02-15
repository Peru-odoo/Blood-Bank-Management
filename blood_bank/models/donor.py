from odoo import fields, models

class donorInfo(models.Model):
    _name = "donor.info"
    _description = "Donor Information"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"

    name = fields.Char(required=True)
    blood_group = fields.Selection(
        string='Blood Group',
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
    age = fields.Integer(required=True)
    weight = fields.Float(string="Weight (kg)", required=True)
    last_donated = fields.Date(string="Last Donted On")
    report = fields.Binary()
