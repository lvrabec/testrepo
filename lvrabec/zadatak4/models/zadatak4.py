# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zadatak4(models.Model):
    _inherit=['hr.department']
    name=fields.Char(track_visibility='onchange')
