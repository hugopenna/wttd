from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    data = dict()
    def setUp(self):
        data = dict(name='Paul Walker', cpf='12345678901', email='me@me.com', phone='11999991234')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@hugopenna.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@hugopenna.com', 'me@me.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Paul Walker',
            '12345678901',
            'me@me.com',
            '11999991234'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
