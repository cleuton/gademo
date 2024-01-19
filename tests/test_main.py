import unittest
from app.main import app

class FlaskTest(unittest.TestCase):

    # Executado antes de cada teste
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # Testa se a resposta é 200 OK
    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Testa o conteúdo da resposta
    def test_home_data(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello, Flask!')

if __name__ == '__main__':
    unittest.main()
