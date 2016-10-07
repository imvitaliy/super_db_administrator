from selenium import webdriver

from django.test import LiveServerTestCase
from django.conf import settings


class SuperDBTestCase(LiveServerTestCase):

    def setUp(self):
        chromedriver = settings.BASE_DIR+'/chromedriver'
        print(chromedriver)
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_rebenton(self):
        self.fail("Test rebenton, por implementar")
