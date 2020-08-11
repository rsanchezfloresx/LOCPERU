# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class FacturaElectronica(models.Model):
    _name = 'loc_pe.fe'
    _description = 'Factura Electronica'

    # your file will be stored here:
    #csv_file = fields.Binary(string='CSV File', required=True)
    code = fields.Char(string="Codigo", required=True)
    name = fields.Char(string="Descripcion", required=True)

    #@api.multi
    #def import_csv(self):
    #    # this will get executed when you click the import button in your form
    #    print("yes working")
    #    return {}