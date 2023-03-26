from django.test import TestCase
from rest_framework.test import APIClient


class ProductsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_products(self):
        response = self.client.get('/api/products/', {'keyword': 'test', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('products' in response.data)
        self.assertTrue('page' in response.data)
        self.assertTrue('pages' in response.data)
        self.assertIsInstance(response.data['products'], list)
        self.assertIsInstance(response.data['page'], int)
        self.assertIsInstance(response.data['pages'], int)

    def test_search_products_no_results(self):
        response = self.client.get('/api/products/', {'keyword': 'nonexistent', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['products'], [])

    def test_search_products_page_size(self):
        response = self.client.get('/api/products/', {'keyword': 'test', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['products']), 0)

    def test_search_products_multi_word_query(self):
        response = self.client.get('/api/products/', {'keyword': 'test product', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data['products']) == 0)
