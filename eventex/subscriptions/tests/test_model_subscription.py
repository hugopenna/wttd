from datetime import datetime

from django.shortcuts import resolve_url as r

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Paul Walker',
                cpf='12345678901',
                email='me@me.com',
                phone='11999991234',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Paul Walker', str(self.obj))

    def test_paid_default_to_False(self):
        """By Default paid must be false"""
        self.assertEqual(False, self.obj.paid)

    def test_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())