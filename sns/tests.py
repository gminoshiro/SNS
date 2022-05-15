from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Group, Message

class SnsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        ……変更ないため省略……

    @classmethod
    def create_user_and_group(cls):
        ……変更ないため省略……

    @classmethod
    def create_message(cls, usr, grp):
        ……変更ないため省略……

    def test_check(self):
        usr = User.objects.filter(username='test').first()

        # access to SNS.
        response = self.client.get(reverse('index'))
        self.assertIs(response.status_code, 302)

        # login test account and access to SNS.
        self.client.force_login(usr)
        response = self.client.get(reverse('index'))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, 'this is test message.')
