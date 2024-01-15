# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmploymnetDate(models.Model):
    # _name = 'hr.employee'
    _inherit='hr.employee'

    datum=fields.Date(string='Date of Employment')
