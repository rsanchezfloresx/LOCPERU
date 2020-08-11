# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class FacturaElectronicaImport(models.Model):
    _name = 'loc_pe.fe_import'
    _description = 'Importar CSV'

    # your file will be stored here:
    csv_file = fields.Binary(string='CSV File', required=True)

    def import_csv(self):
        # this will get executed when you click the import button in your form
        print("yes working")
        return {}