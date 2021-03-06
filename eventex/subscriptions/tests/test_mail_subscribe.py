from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    data = dict()
    def setUp(self):
        data = dict(name='Hugo Penna', cpf='12345678901', email='wttd@hugopenna.com', phone='11-99998-1254')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@hugopenna.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@hugopenna.com', 'wttd@hugopenna.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Hugo Penna',
            '12345678901',
            'wttd@hugopenna.com',
            '11-99998-1254'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
