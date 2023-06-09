# -*- coding: utf-8 -*-
from odoo.odoo import models, fields


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'TestModel'

    name = fields.Char('Hello')



