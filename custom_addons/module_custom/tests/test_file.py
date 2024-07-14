from odoo.exceptions import ValidationError
from odoo.tests import tagged, TransactionCase


@tagged('-at_install', 'post_install')
class TestModuleee(TransactionCase):
     def setUp(self):
        pass

     def test_create_works(self):
          rec = self.env['test.model'].create({
            "name": "test_name"
        })
          self.assertEqual(rec.number, 50)
