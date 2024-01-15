# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zadatak3(models.Model):
    _inherit='hr.employee'

    @api.multi
    @api.depends('ime','prezime')
    def izrcunajIme(self):
        for i in self:
            self.env.cr.execute("""select value from ir_config_parameter where key='zadatak3.setting_field' """)
            result = self.env.cr.fetchone()
            if result:
                value=result[0]
                for record in self: # reducirati iteracije 
                    record.name=f"{record.prezime} {record.ime}"
                    
            else:

                for record in self:             
                    record.name=f"{record.ime} {record.prezime}"

    ime=fields.Char(string='Ime zaposlenika', required=True)
    prezime=fields.Char(string='Prezime zaposlenika',required=True)
    name=fields.Char(compute="izrcunajIme", readonly=True, store=False, related=False)

