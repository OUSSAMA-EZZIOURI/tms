# See LICENSE file for full copyright and licensing details.

# import time
import calendar
import re

from odoo import api, fields, models


class TransportFDP(models.Model):
    """Final Delivery Point"""

    _name = "transport.fdp"
    _description = "Final Delivery Point"
    _order = "name"

    name = fields.Char(
        "name",
        help="Final Delivery Point",
    )
    country_id = fields.Many2one(
        "res.country",
        "Destination country",
        ondelete="cascade",
        required=True,
        help="Destination country",
    )

    def name_get(self):
        return [(rec.id, rec.name + " [" + rec.country_id.code + "]") for rec in self]
