from odoo import models, fields, api

class napredno(models.TransientModel):
    _inherit = 'res.config.settings'

    setting_field = fields.Boolean(string='name_surname_toggle', config_parameter='zadatak3.setting_field')

