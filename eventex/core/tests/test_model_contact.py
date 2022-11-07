from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speakers, Contacts

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speakers.objects.create(
            name= 'Henrique Bastos',
            slug= 'henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contacts.objects.create(speaker=self.speaker, kind=Contacts.EMAIL,
                                          value='henrique@bastos.net')

        self.assertTrue(Contacts.objects.exists())

    def test_phone(self):
        contact = Contacts.objects.create(speaker=self.speaker, kind=Contacts.PHONE,
                                          value='12123451234')

        self.assertTrue(Contacts.objects.exists())

    def test_choices(self):
        contact = Contacts(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contacts(speaker=self.speaker, kind=Contacts.EMAIL, value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speakers.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

        s.contacts_set.create(kind=Contacts.EMAIL, value='henrique@bastos.net')
        s.contacts_set.create(kind=Contacts.PHONE, value='11-99999-1234')

    def test_email(self):
        qs = Contacts.emails.all()
        expected = ['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contacts.phones.all()
        expected = ['11-99999-1234']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)