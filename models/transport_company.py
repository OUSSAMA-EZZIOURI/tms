
from odoo import api, fields, models

class TransportCompany(models.Model):
    _name = 'transport.company'
    _inherit = 'res.company'
    _description = "Transport Company"
    is_transport_company = fields.Boolean(
        "is_transport_company",
        default='True',
        help="Is it a transport company ?"
    )
    user_ids = fields.Many2many('res.users', 'transport_company_users_rel', 'cid', 'user_id', string='Accepted Users')
    # channel_ids = fields.Many2many("mail.channel", "mail_channel_profile_partner", "partner_id", "channel_id",
    #                                copy=False)
    # meeting_ids = fields.Many2many('calendar.event', 'calendar_event_profile_res_partner_rel', 'res_partner_id',
    #                                'calendar_event_id', string='Meetings', copy=False)

