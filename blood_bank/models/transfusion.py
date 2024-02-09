from odoo import fields, models

class transfusionBlood(models.Model):
    _name = "transfusion.blood"
    _description = "Transfusion Blood"

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
    date_tranfusion = fields.Date(required=True, string="Date of Transfusion")
    hospital = fields.Char(required=True, string="Hospital's Name")
    quantity_req = fields.Float(required=True, string="Blood Quantity Required (ml)")
    purpose_transfusion = fields.Char(string="Purpose of Tranfusion")
