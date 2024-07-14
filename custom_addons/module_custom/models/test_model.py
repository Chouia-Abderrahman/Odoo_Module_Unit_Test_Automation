# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from datetime import datetime, timedelta
from odoo import _, models
from odoo.exceptions import AccessDenied, UserError
from odoo.http import request
from odoo.tools.misc import babel_locale_parse, hmac
from odoo.odoo import fields


class TestModule(models.Model):
    _name = 'test.model'

    name = fields.Char(required=True)
    number = fields.Integer(default=50)
