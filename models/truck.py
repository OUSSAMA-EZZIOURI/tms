# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


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

    name = fields.Char(
        "name",
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
        "transport.company",
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
        return [(rec.id, rec.trans_company_id.name + " / " + rec.container_plate ) for rec in self]

    @api.model
    def create(self, vals):
        # Modify the values before creating the record
        vals['company_name'] = self.trans_company_id.name
        return super(TransportTruck, self).create(vals)

    def write(self, vals):
        # Use the browse() method to retrieve the record
        #vals['company_name'] = self.env['transport.company'].browse(vals['trans_company_id']).name
        vals['company_name'] = self.trans_company_id.name
        return super(TransportTruck, self).write(vals)

    @api.onchange('trans_company_id')
    def _onchange_trans_company_id(self):
        # Perform actions when field1 changes
        self.company_name = self.trans_company_id.name
