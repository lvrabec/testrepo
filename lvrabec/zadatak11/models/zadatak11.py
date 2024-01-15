# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zadatak11(models.Model):
    _name = 'zadatak11.zadatak11'
  



    zaposlenik=fields.Many2one(comodel_name='hr.employee',string='Zaposlenik')
    pocetni_datum=fields.Date(string='Pocetni Datum')
    zavrsni_datum=fields.Date(string='Završni Datum')
    polaziste=fields.Char(string='Polazište')
    odrediste=fields.Char(string='Odrediste')
    state=fields.Selection([('nac','Nacrt'),('zav','Zavrseno')],string='Status',default='nac')

    @api.depends('state')
    def status_change(self):
        print(self.state)
        self.state = 'zav'
        print(self.state)


    @api.onchange('pocetni_datum')
    @api.depends('zavrsni_datum')
    def _date_change(self):
        print ('Zavrsni datum je', self.zavrsni_datum)
        if self.zavrsni_datum == False:
            print('ide grananje')
            self.zavrsni_datum = self.pocetni_datum
        