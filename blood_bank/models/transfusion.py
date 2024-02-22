from odoo import fields, models

class transfusionBlood(models.Model):
    _name = "transfusion.blood"
    _description = "Transfusion Blood"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "hospital"

    patient_name = fields.Char(required=True, string="Patient Name")
    blood_group_transfused = fields.Selection(
        string="Blood Group Transfused",
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
    date_tranfusion = fields.Date(required=True, string="Date of Transfusion")
    hospital = fields.Char(required=True, string="Hospital's Name")
    quantity_transfused = fields.Float(required=True, string="Blood Transfused (ml)")
    purpose_transfusion = fields.Char(string="Purpose of Tranfusion")
    aadhar_no = fields.Char(required=True, copy=False)
