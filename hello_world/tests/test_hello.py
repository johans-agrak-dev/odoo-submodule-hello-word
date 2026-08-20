from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestHelloController(HttpCase):

    def test_hello_route_returns_greeting(self):
        response = self.url_open('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, World!', response.text)

    def test_hello_route_rejects_non_get_methods(self):
        response = self.url_open('/hello', method='POST')
        self.assertEqual(response.status_code, 405)
