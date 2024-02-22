from odoo import models, fields

class BloodBankLocation(models.Model):
    _name = "location.blood"
    _description = "Blood Bank Location"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Location Name", required=True)
