# -*- coding: utf-8 -*-

from odoo import models, fields, api


class zadatak5(models.Model):
    _inherit=['hr.employee']

    children_ids=fields.One2many(comodel_name='djeca.djeca',string='Podaci o djeci', inverse_name="employee_id")

