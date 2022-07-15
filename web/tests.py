from django.test import TestCase
# Create your tests here.
from django.urls import reverse

from web.utils import encode_base62, decode_base62


class TestBase62(TestCase):
    def test_encode(self):
        result = encode_base62(123)
        self.assertEqual(result, "4d")

    def test_decode(self):
        result = decode_base62("4d")
        self.assertEqual(result, 123)


class TestPage(TestCase):
    def test_creation(self):
        response = self.client.post(reverse('page'), {"url": "https://google.com"})

        self.assertContains(response, "http://testserver/3", 2, 200)

    def test_redirect(self):
        self.client.post(reverse('page'), {"url": "https://google.com"})
        response = self.client.get(reverse('redirect', kwargs={'slug': 3}))

        self.assertRedirects(response, "https://google.com", 302, fetch_redirect_response=False)

    def test_clicks(self):
        self.client.post(reverse('page'), {"url": "https://google.com"})
        self.client.get(reverse('redirect', kwargs={'slug': 3}))
        self.client.get(reverse('redirect', kwargs={'slug': 3}))
        response = self.client.post(reverse('page'), {"url": "https://google.com"})

        self.assertContains(response, "http://testserver/3", 2, 200)
        self.assertContains(response, "Clicks: 2", 1, 200)




