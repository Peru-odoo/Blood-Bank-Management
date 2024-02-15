from odoo import api, fields, models

class donationInfo(models.Model):
    _name = "donation.info"
    _description = "Donation Information"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "donation_center"

    name = fields.Char(required=True, string="Doner Name")
    donation_date = fields.Date(string="Donation Date")
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
    donation_center = fields.Char(string="Donation Center")
    quantity = fields.Float(string="Blood Donated (ml)", required=True)

    @api.onchange('donation_date', 'donation_center')
    def _onchange_donation_fields(self):
        if self.donation_date:
            return {'required': {'donation_center': True}}
        else:
            return {'required': {'donation_center': False, 'donation_center': False}}
