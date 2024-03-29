from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speakers


class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speakers.objects.create(
            name='Grace Hopper',
            description='Programadora e Almirante',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            slug='grace-hopper'
        )
        self.resp = self.client.get(r('speakers_detail', slug='grace-hopper'))

    def test_get(self):
        """GET should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'core/speakers_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e Almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """Speaker must be in context"""
        speakers = self.resp.context['speakers']
        self.assertIsInstance(speakers, Speakers)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speakers_detail', slug='not_found'))
        self.assertEqual(404, response.status_code)