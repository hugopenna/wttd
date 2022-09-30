from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminClass(TestCase):
    def test_has_action(self):
        """Action mark_as_paid shuld be installed"""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected as paid"""
        Subscription.objects.create(name='paul walker', cpf='12345678901', email='me@me.com', phone='11999991234')
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)

        queryset = Subscription.objects.all()

        model_admin.mark_as_paid(None, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
