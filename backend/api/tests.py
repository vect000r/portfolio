from datetime import date

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import Experience


class ExperienceApiTests(APITestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            company='Example Labs',
            role='Software Engineer',
            start_date=date(2022, 1, 1),
            technologies=['Django', 'React'],
        )

    def test_experience_list_is_public(self):
        response = self.client.get('/api/experience/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['company'], 'Example Labs')
        self.assertEqual(response.data[0]['years_display'], '2022 - Present')

    def test_experience_changes_require_admin(self):
        response = self.client.post(
            '/api/experience/',
            {
                'company': 'Other Labs',
                'role': 'Developer',
                'start_date': '2024-01-01',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 403)

    def test_admin_can_create_experience(self):
        user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='secure-test-password',
        )
        self.client.force_authenticate(user=user)

        response = self.client.post(
            '/api/experience/',
            {
                'company': 'New Labs',
                'role': 'Senior Developer',
                'start_date': '2024-01-01',
                'technologies': ['Python'],
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)
