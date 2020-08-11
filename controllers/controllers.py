# -*- coding: utf-8 -*-
# from odoo import http


# class LocPeruFe(http.Controller):
#     @http.route('/loc_peru_fe/loc_peru_fe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_peru_fe/loc_peru_fe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_peru_fe.listing', {
#             'root': '/loc_peru_fe/loc_peru_fe',
#             'objects': http.request.env['loc_peru_fe.loc_peru_fe'].search([]),
#         })

#     @http.route('/loc_peru_fe/loc_peru_fe/objects/<model("loc_peru_fe.loc_peru_fe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_peru_fe.object', {
#             'object': obj
#         })
