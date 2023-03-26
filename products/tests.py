# from rest_framework.test import APITestCase
# from rest_framework import status
#
#
# class ProductSearchTestCase(APITestCase):
#     def setUp(self):
#         self.product1 = {
#             "_id": "641db4431324f541667ae5b8",
#             "gender": "women",
#             "product_id": "AE0APMM1670000000000_ΓΚΡΙ_AE0-GREY",
#             "product_title": "T-shirt 'Roll Sleeve' AEROPOSTALE",
#             "product_description": "T-shirt AEROPOSTALE σε γκρι χρώμα. Στρογγυλή λαιμόκοψη και τύπωμα λογότυπο στο στήθος.",
#             "brand": "AEROPOSTALE",
#             "source": "shopntrade",
#             "product_categories": [
#                 "ΓΥΝΑΙΚΕΙΟ > ΜΠΛΟΥΖΑ > T-SHIRT"
#             ],
#             "url": "https://www.bloobox.gr/el-gr/gunaikeio-mplouza-t-shirt/t-shirt-roll-sleeve-aeropostale-599568",
#             "price": 19,
#             "discount": 0.39999999999999997,
#             "currency_code": "EUR",
#             "stock": 1,
#             "stock_level": 1,
#             "additional_ids": [
#                 "AE0APMM1670000000000_ΓΚΡΙ",
#                 "MM16700000-GREY"
#             ],
#             "image_urls": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568__3475551.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568_2.jpg"
#             ],
#             "position": [
#                 "undefined",
#                 "undefined",
#                 "undefined"
#             ],
#             "product_imgs_src": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568__3475551.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599568_2.jpg"
#             ],
#             "images": [
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599568__3475551.jpg",
#                     "path": "images/1688409e3a9c83c9f06037afa3fba604b1b1dfa6.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/1688409e3a9c83c9f06037afa3fba604b1b1dfa6.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/1688409e3a9c83c9f06037afa3fba604b1b1dfa6.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599568.jpg",
#                     "path": "images/d2b2a62ed5230a8e84ae5156d855adf79e9ff2ea.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/d2b2a62ed5230a8e84ae5156d855adf79e9ff2ea.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/d2b2a62ed5230a8e84ae5156d855adf79e9ff2ea.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599568_2.jpg",
#                     "path": "images/6090e19c95d0d0d7f6bac70d7519681476f76280.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/6090e19c95d0d0d7f6bac70d7519681476f76280.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/6090e19c95d0d0d7f6bac70d7519681476f76280.jpg"
#                 }
#             ]
#         }
#
#         self.product2 = {
#             "_id": "641db4431324f541667ae5b9",
#             "gender": "women",
#             "product_id": "AE0APMM1670000000000_ΜΠΛΕ_AE0-NAVY",
#             "product_title": "T-shirt 'Roll Sleeve' AEROPOSTALE",
#             "product_description": "T-shirt AEROPOSTALE σε σκούρο μπλε χρώμα. Στρογγυλή λαιμόκοψη και τύπωμα λογότυπο στο στήθος.",
#             "brand": "AEROPOSTALE",
#             "source": "shopntrade",
#             "product_categories": [
#                 "ΓΥΝΑΙΚΕΙΟ > ΜΠΛΟΥΖΑ > T-SHIRT"
#             ],
#             "url": "https://www.bloobox.gr/el-gr/gunaikeio-mplouza-t-shirt/t-shirt-roll-sleeve-aeropostale-599574",
#             "price": 19,
#             "discount": 0.39999999999999997,
#             "currency_code": "EUR",
#             "stock": 1,
#             "stock_level": 1,
#             "additional_ids": [
#                 "AE0APMM1670000000000_ΜΠΛΕ",
#                 "MM16700000-NAVY"
#             ],
#             "image_urls": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574__3475569.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574_2.jpg"
#             ],
#             "position": [
#                 "undefined",
#                 "undefined",
#                 "undefined"
#             ],
#             "product_imgs_src": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574__3475569.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599574_2.jpg"
#             ],
#             "images": [
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599574__3475569.jpg",
#                     "path": "images/43888e978527e3cbf6b655fb51b9bf5c44c3de7d.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/43888e978527e3cbf6b655fb51b9bf5c44c3de7d.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/43888e978527e3cbf6b655fb51b9bf5c44c3de7d.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599574.jpg",
#                     "path": "images/9ab7acfcb1311c35c771bd396c38827fe31d3631.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/9ab7acfcb1311c35c771bd396c38827fe31d3631.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/9ab7acfcb1311c35c771bd396c38827fe31d3631.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599574_2.jpg",
#                     "path": "images/3b7a29b7dfda2b0edc447cad1b3f3c92db458a7d.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/3b7a29b7dfda2b0edc447cad1b3f3c92db458a7d.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/3b7a29b7dfda2b0edc447cad1b3f3c92db458a7d.jpg"
#                 }
#             ]
#         }
#         self.product3 = {
#             "_id": "641db4431324f541667ae5ba",
#             "gender": "men",
#             "product_id": "AE0APNF4730000000000_ΜΑΥΡΟ_AE0-BLACK",
#             "product_title": "Παντελόνι Φόρμας AEROPOSTALE",
#             "product_description": "Παντελόνι Φόρμας AEROPOSTALE σε μαύρο χρώμα με λευκό μεγάλο λογότυπο στο πλάι. Λάστιχο και κορδόνι προσαρμογής στη μέση. Ελαστικό τελείωμα στους αστράγαλους. Τσέπες στη μέση.",
#             "brand": "AEROPOSTALE",
#             "source": "shopntrade",
#             "product_categories": [
#                 "ΑΝΔΡΙΚΟ > ΠΑΝΤΕΛΟΝΙ > ΑΘΛΗΤΙΚΗ ΦΟΡΜΑ"
#             ],
#             "url": "https://www.bloobox.gr/el-gr/andriko-panteloni-athlhtikh-forma/panteloni-formas-aeropostale-599698",
#             "price": 39,
#             "discount": 0.4,
#             "currency_code": "EUR",
#             "stock": 1,
#             "stock_level": 1,
#             "additional_ids": [
#                 "AE0APNF4730000000000_ΜΑΥΡΟ",
#                 "NF47300000-BLACK"
#             ],
#             "image_urls": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698__3475905.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698_2.jpg"
#             ],
#             "position": [
#                 "undefined",
#                 "undefined",
#                 "undefined"
#             ],
#             "product_imgs_src": [
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698__3475905.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698.jpg",
#                 "https://www.bloobox.gr/Images/Products/Normal/590000/599698_2.jpg"
#             ],
#             "images": [
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599698__3475905.jpg",
#                     "path": "images/2c61498b29919a17355cc7b1ea751533171a12cc.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/2c61498b29919a17355cc7b1ea751533171a12cc.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/2c61498b29919a17355cc7b1ea751533171a12cc.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599698.jpg",
#                     "path": "images/cc23cb6ccece37db08332f792774fa79dff65176.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/cc23cb6ccece37db08332f792774fa79dff65176.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/cc23cb6ccece37db08332f792774fa79dff65176.jpg"
#                 },
#                 {
#                     "url": "https://www.bloobox.gr/Images/Products/Normal/590000/599698_2.jpg",
#                     "path": "images/577dec6e38ae4f5863d27fc08f66059ff2b48e01.jpg",
#                     "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/577dec6e38ae4f5863d27fc08f66059ff2b48e01.jpg",
#                     "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/577dec6e38ae4f5863d27fc08f66059ff2b48e01.jpg"
#                 }
#             ]
#         }
#
#     def test_api_can_search_products(self):
#         url = '/api/products/'
#         response = self.client.get(url, {'keyword': 'shi'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['products']), 2)
#         self.assertEqual(response.data['products'][0]['product_title'], 'shir')
#
#     def test_api_returns_empty_list_when_no_matching_products(self):
#         url = '/api/products/'
#         response = self.client.get(url, {'keyword': 'NonexistentProduct'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['products']), 0)

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
