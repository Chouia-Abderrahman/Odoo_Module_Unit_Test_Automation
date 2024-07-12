from odoo.exceptions import ValidationError
from odoo.tests import tagged

from odoo.odoo.tests import TransactionCase


@tagged('-at_install', 'post_install')
class TestArchiveReason(TransactionCase):

    def test_create_works(self):
        rec = self.env['test.model'].create({
            "name": "test_name"
        })
        self.assertEquals(rec.number, 50)
