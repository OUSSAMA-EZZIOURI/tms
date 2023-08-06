# See LICENSE file for full copyright and licensing details.

import calendar
import re

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.translate import _


class TransportDepartures(models.Model):
    """Define the departure schedule"""

    _name = "transport.departure"
    _description = "Transport Departure"
    _order = "date_exp_departure"

    def _default_container_id(self):
        return self.env['transport.truck'].search([('container_plate', '=', '?')], limit=1).id

    def _default_container_plate(self):
        rec = self.env['transport.truck'].search([('container_plate', '=', '?')], limit=1)
        return rec.container_plate
    container_id = fields.Many2one(
        "transport.truck",
        "Container",
        index=True, ondelete='cascade',
        default=_default_container_id,
        help="""The planned container for this departure""",
    )
    urgent_part = fields.Boolean(
        "Urgent part ?",
        help="Is the truck will transport some urgent part ?",
    )
    fdp_id = fields.Many2one(
        "transport.fdp",
        "Final Destination",
        required=True,
        help="The final delivery point",
    )
    date_exp_departure = fields.Date(
        "Expected Departure Date", required=True, help="Expected Date of departure"
    )
    time_exp_departure = fields.Char(string="Expected Time of Departure", required=True)
    date_departure = fields.Date("Departure Date", help="The real Departure Date" )
    time_departure = fields.Char(string='Time of Departure')
    state = fields.Selection([('draft', 'Draft'), ('planned', 'Planned')
                                  , ('on_site', 'On-site')
                                  , ('in_process', 'In process')
                                 , ('departed', 'Departed')
                                  , ('cancelled', 'Cancelled'),
                              ('delay', 'Delay')]
                              , required=True,
                              copy=False,
                              tracking=True, default='draft',
                              help="State")
    attachement= fields.Binary(string="Attachement")
    fname_attachement= fields.Char(string="File name attachement")

    def action_set_as_planned(self):
        for rec in self:
#            if rec.state not in ['planned', 'on_site', 'in_process', 'departed', 'departed_issue', 'cancelled']:
#                continue
            rec.write({'state': 'planned'})
        return True

    def action_set_as_on_site(self):
        for rec in self:
#            if rec.state not in ['draft', 'planned', 'on_site', 'in_process', 'departed', 'departed_issue', 'cancelled']:
#                continue
            rec.write({'state': 'on_site'})
        return True

    def action_set_as_in_process(self):
        for rec in self:
#            if rec.state not in ['draft', 'in_process', 'on_site', 'departed', 'departed_issue', 'cancelled']:
#                continue
            rec.write({'state': 'in_process'})
        return True

    def action_set_as_departed(self):
        for rec in self:
            #            if rec.state not in ['draft', 'in_process', 'on_site', 'departed', 'departed_issue', 'cancelled']:
            #                continue
            rec.write({'state': 'departed'})
        return True

    def action_set_as_cancelled(self):
        for rec in self:
            #            if rec.state not in ['draft', 'in_process', 'on_site', 'departed', 'departed_issue', 'cancelled']:
            #                continue
            rec.write({'state': 'cancelled'})
        return True

    def name_get(self):
        for rec in self:
            if False == rec.container_id.container_plate:
                print ("ducky is False")
                print(self._default_container_plate())
                print(self._default_container_id())
                return [(self._default_container_id(), self._default_container_plate() + " / " + rec.fdp_id.name)]
            else:
                print("ducky is " + rec.container_id.container_plate)
                print("Company" + rec.container_id.trans_company_id.name)
                print("Short desc" + rec.container_id.name)
                return [(rec.id, rec.container_id.container_plate + " / " + rec.fdp_id.name + " / ")]


    @api.model
    def create(self, vals):
        # Modify the values before creating the record
        print(vals)
        if False == vals['container_id']:
            vals['container_id'] = self._default_container_id()
        return super(TransportDepartures, self).create(vals)

# return [(rec.id, rec.container_id.container_plate + " / " + rec.fdp_id.name) for rec in self]
