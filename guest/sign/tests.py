#-*- coding：utf-8 -*-

from django.test import TestCase, Client
from sign.models import Event, Guest
from django.contrib.auth.models import User

class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="红米note7 pro plus", limit=2000, status=True, address="深圳",
                             start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, realname="悠悠", phone='13206798080', email='yy@email.com',
                             sign=False, event_id=1)

    def test_event_models(self):
        result = Event.objects.get(name="红米note7 pro plus")
        self.assertEqual(result.address, "深圳")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13206798080')
        self.assertEqual(result.realname, "悠悠")
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        """测试index视图"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user("admin", "admin@email.com", "admin123")

    def test_login_action_username_password_null(self):
        test_data = {'username':'', 'password':''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        test_data = {'username':'aaa', 'password':'12356'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_success(self):
        test_data = {'username':'admin', 'password':'admin123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)
