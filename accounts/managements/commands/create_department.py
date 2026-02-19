from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample users for each department'

    def handle(self, *args, **options):
        departments = [
            {'username': 'admin1', 'email': 'admin@tficms.local', 'dept': 'admin', 'is_staff': True, 'is_superuser': True},
            {'username': 'doctor1', 'email': 'doctor@tficms.local', 'dept': 'doctor', 'is_staff': True},
            {'username': 'nurse1', 'email': 'nurse@tficms.local', 'dept': 'nurse', 'is_staff': True},
            {'username': 'pharmacist1', 'email': 'pharmacist@tficms.local', 'dept': 'pharmacy', 'is_staff': True},
            {'username': 'receptionist1', 'email': 'receptionist@tficms.local', 'dept': 'reception', 'is_staff': True},
        ]

        for dept in departments:
            if not User.objects.filter(username=dept['username']).exists():
                User.objects.create_user(
                    username=dept['username'],
                    email=dept['email'],
                    password='Password123!',
                    department=dept['dept'],
                    is_staff=dept.get('is_staff', False),
                    is_superuser=dept.get('is_superuser', False),
                )
                self.stdout.write(f"✅ Created {dept['username']}")
            else:
                self.stdout.write(f"⏭️ {dept['username']} already exists")