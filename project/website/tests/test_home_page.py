import socket

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import resolve

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from project.website.views import index


class BaseTestCase(StaticLiveServerTestCase):
    """
    Provides base test class which connects to the Docker
    container running selenium.
    """
    host = '0.0.0.0' # Bind to 0.0.0.0 to allow external access

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.host = socket.gethostbyname(socket.gethostname())

        cls.selenium = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

class HomePageTest(BaseTestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        self.live_server_url = self.live_server_url
        self.selenium.get(self.live_server_url)

        html = self.selenium.page_source
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Kabiria</title>', html)
        self.assertTrue(html.endswith('</html>'))
