# See LICENSE file for full copyright and licensing details.

# import time
import calendar
import re

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.translate import _


class ContainerType(models.Model):
    """Container type"""

    _name = "transport.container.type"
    _description = "Container Type"
    _order = "name"

    name = fields.Char(
        "name",
        help="The plate of the truck",
    )


class TransportTruck(models.Model):
    """Defines the trucks used for inbond or outbound"""

    _name = "transport.truck"
    _description = "Transport Truck"
    _order = "container_plate"

    truck_plate = fields.Char(
        "truck_plate",
        help="The plate of the truck",
    )
    container_plate = fields.Char(
        "container_plate",
        required=True,
        help="The plate of the container",
    )
    container_type = fields.Selection([('bache', 'Bâchée'), ('tolee', 'Tôlée'), ('van', 'Van'), ('minitir', 'Mini-tir')]
                                      , required=True,
                                      help="Container type")
    trans_company_id = fields.Many2one(
        "res.partner",
        "Transport Company",
        ondelete="cascade",
        required=True,
        help="Company_id of the truck",
    )
    company_name = fields.Char(
        "Company Name",
        help="Transport Company name",
    )

    def name_get(self):
        return [(rec.id, rec.container_plate) for rec in self]

    @api.model
    def create(self, vals):
        # Modify the values before creating the record
        vals['company_name'] = self.trans_company_id.name
        return super(TransportTruck, self).create(vals)

    def write(self, vals):
        # Use the browse() method to retrieve the record
        vals['company_name'] = self.env['res.partner'].browse(vals['trans_company_id']).name
        return super(TransportTruck, self).write(vals)

    @api.onchange('trans_company_id')
    def _onchange_trans_company_id(self):
        # Perform actions when field1 changes
        self.company_name = self.trans_company_id.name
