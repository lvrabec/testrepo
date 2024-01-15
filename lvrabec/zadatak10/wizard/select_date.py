from odoo import models, fields, api

class SelectDateWizard(models.TransientModel):
    _name='select.date.wizard'
    _description='Wizzard za zadatak 10'


    user_selected_date =fields.Date(string='Datum')

    @api.multi
    def setDate(self):
        contracts = self.env['hr.contract'].browse(self._context.get("active_ids"))
        contracts.write({'date_end': self.user_selected_date})
        return {'type': 'ir.actions.act_window_close'}

