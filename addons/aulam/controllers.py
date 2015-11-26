# -*- coding: utf-8 -*-
from openerp import http

# class Aulam(http.Controller):
#     @http.route('/aulam/aulam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aulam/aulam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aulam.listing', {
#             'root': '/aulam/aulam',
#             'objects': http.request.env['aulam.aulam'].search([]),
#         })

#     @http.route('/aulam/aulam/objects/<model("aulam.aulam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aulam.object', {
#             'object': obj
#         })