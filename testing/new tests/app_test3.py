import unittest
from app import app, flight_cart

class TestFlights(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.selected_flights = ['1', '2']

    def test_cart_POST(self):
        with app.test_client() as client:
            response = client.post('/cart', data={'flight_id': self.selected_flights})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(flight_cart), 2)

if __name__ == '__main__':
    unittest.main()
