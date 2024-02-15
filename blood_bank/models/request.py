from odoo import fields, models

class requestBlood(models.Model):
    _name = "request.blood"
    _description = "Request Blood"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "hospital"

    patient_name = fields.Char(required=True, string="Patient Name")
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
    hospital = fields.Char(required=True, string="Hospital's Name")
    urgency = fields.Selection(
        [
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('month_later', 'After a month')
        ],
        string='Urgency', default='normal'
    )
    request_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ],
        string='Request Status', default='pending'
    )
    quantity_req = fields.Float(string="Blood Quantity Required (ml)", required=True)
