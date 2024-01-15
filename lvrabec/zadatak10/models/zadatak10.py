# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api

class zadatak10(models.Model):
    _name='hr.contract'
    _inherit="hr.contract"


    def ugovor(self):
        self.date_end= date.today()
        self.write({
            'state': 'close'
        })
      
    
    def launch_wiz(self):
        action=self.env.ref('zadatak10.select_date_wizard').read()[0]
        self.write({
            'state':'close'
        })
        return action
  
