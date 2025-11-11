import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug 
if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Criação do cliente de teste 
        cls.client = app.test_client()
    
    def test_post_to_home_route_should_get_method_not_allowed(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

    def test_get_to_login_route_should_get_method_not_allowed(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 405)

    def test_get_to_protected_route_without_jwt_should_not_be_200(self):
        response = self.client.get('/protected')
        self.assertNotEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
