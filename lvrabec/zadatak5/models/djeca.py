# -*- coding: utf-8 -*-

from odoo import models, fields, api
    
class djeca(models.Model):
    _name='djeca.djeca'
   
    

    ime_djeteta=fields.Char(string='Ime Djeteta')
    prezime_djeteta=fields.Char(string='Prezime Djeteta')
    dob=fields.Date(string='Datum rođenja')

    employee_id=fields.Many2one(comodel_name="hr.employee",string='employee')