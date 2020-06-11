#basit test yapısı import edildi
from django.test import SimpleTestCase

# Create your tests here.

#basit olarak sayfaların status kodlarının 200 (OK)
#olup olmadığını kontrol eder
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code,200)
