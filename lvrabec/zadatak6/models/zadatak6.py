# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zadatak6(models.Model):
    _inherit=['hr.employee']    
    oib=fields.Char(string='OIB')


    _sql_constraints = [
            ('oib_check_slova', 'CHECK(oib ~ E\'^[0-9]+$\'::text)', 'OIB mora sadržavati samo brojeve.'),
            ('oib_check_duljina', 'CHECK(length(oib) = 11)', 'Duljina OIB-a mora biti 11 znakova.')
        ]
