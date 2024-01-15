# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NapredniReport(models.Model):
    _name='report.zadatak9.report_hr_employee_napredno' # report.module_name.report_name    
    _description='Report za napredno'
    _inherit='hr.employee'

    @api.model
    def _get_report_values(self, docids, data=None):
        all_employees = self.env['hr.employee'].browse(docids)
        extract_name = self.env['hr.employee'].search([('name','=',docids[0])])


        lista_employeea= []
        sortana_lista=[]

        for i in all_employees:
            loop_name=i.name
            department_name= i.department_id.name
            dofc=i.datum
            dob=i.birthday

            lista_employeea.append([loop_name,department_name,dofc,dob])
        

        sortana_lista= sorted(lista_employeea,key=lambda x:x[1])
        print('lista1: ', sortana_lista)


        return {
            'doc_ids':docids,
            'doc_model': 'hr.employee',
            'data': data,
            'docs': sortana_lista,
        }
    