from odoo import http


class HelloWorldController(http.Controller):

    @http.route('/hello', type='http', auth='public', methods=['GET'])
    def hello(self):
        return 'Hello, World!'
