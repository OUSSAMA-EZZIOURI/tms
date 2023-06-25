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
    #    container_type = fields.Char(
    #        "container_type",
    #        required=True,
    #        help="Container type",
    #    )
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

#    def name_get(self):
#        return [(rec.id, rec.container_plate) for rec in self]
