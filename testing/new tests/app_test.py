import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_book_flights(self):
        response = self.app.get('/book-flights')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Flights', response.data)

    def test_book_flight(self):
        response = self.app.post('/', data={'city_1': 'New York', 'city_2': 'London'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Available Flights', response.data)

    def test_manage_flights(self):
        response = self.app.get('/manage-flights?flight_id=1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flight Details', response.data)

    def test_cart(self):
        response = self.app.post('/cart', data={'flight_id': '1234'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cart', response.data)

    def test_book_flight_no_input(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please select your origin and destination cities', response.data)

    def test_manage_flights_no_id(self):
        response = self.app.get('/manage-flights')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Flights', response.data)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTestCase)
    with open('app_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
