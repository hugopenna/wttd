from django.test import TestCase


class SpeakerDetailGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/palestrantes/grace-hopper/')

    def test_get(self):
        """GET should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')
