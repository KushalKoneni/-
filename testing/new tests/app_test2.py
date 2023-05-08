import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

def test_invalid_url(self):
    response = self.app.get('/invalid-url')
    self.assertEqual(response.status_code, 404)
    self.assertIn(b'Page Not Found', response.data)

def test_empty_cart(self):
    response = self.app.get('/cart')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Your cart is empty', response.data)

def test_remove_from_cart(self):
    response = self.app.post('/cart', data={'flight_id': '1234', 'action': 'remove'})
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Removed flight 1234 from your cart', response.data)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTestCase)
    with open('app_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
