from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.accounts.models import TelegramIdentity


User = get_user_model()


class UserModelTests(TestCase):
    def test_create_user_with_telegram_identity(self):
        user = User.objects.create_user(
            username="tg_123456789",
            display_name="Test User",
        )

        identity = TelegramIdentity.objects.create(
            user=user,
            telegram_id=123456789,
            username="test_user",
            first_name="Test",
            language_code="fa",
        )

        self.assertEqual(identity.user, user)
        self.assertEqual(user.telegram_identity.telegram_id, 123456789)
        self.assertEqual(str(identity), "@test_user")
        self.assertEqual(str(user), "Test User")

    def test_user_without_display_name_uses_username(self):
        user = User.objects.create_user(
            username="tg_987654321",
        )

        self.assertEqual(str(user), "tg_987654321")
