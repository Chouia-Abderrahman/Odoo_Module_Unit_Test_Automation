# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, exceptions, _


class TestModule(models.Model):
    _name = 'test.model'

    name = fields.Char(required=True)
    number = fields.Integer(default=50)
