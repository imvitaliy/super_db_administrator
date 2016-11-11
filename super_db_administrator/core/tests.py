from selenium import webdriver

from django.test import LiveServerTestCase, TestCase
from django.conf import settings
from django.core.urlresolvers import resolve

from .models import Entity
from .views import IndexView


class SuperDBTestCase(LiveServerTestCase):

    def setUp(self):
        chromedriver = settings.BASE_DIR+'/../chromedriver'
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_in_index(self):
        home_page = self.browser.get(self.live_server_url + '/')
        title_element = self.browser.find_element_by_css_selector('#main_heading')
        self.assertEqual('SuperDB Administrator', title_element.text)


class CoreURLsTestCase(TestCase):

    def test_root_url(self):
        root = resolve('/')
        self.assertEqual(root.func, IndexView.as_view())


class EntityTestCase(TestCase):

    def setUp(self):
        e1 = Entity.objects.create(name="Sevilla")
        e2 = Entity.objects.create(name="Sevilla")

    def test_entities_unique(self):
        entities = Entity.objects.filter(slug="sevilla")
        self.assertEqual(entities.count(), 1)

    def test_not_equals_slugs(self):
        entities = Entity.objects.filter(name="Sevilla")
        self.assertEqual(entities.count(), 2)
        self.assertNotEqual(entities[0].slug, entities[1].slug)
