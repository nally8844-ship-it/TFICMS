import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tficms.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.create_superuser(
    username='admin',
    email='admin@tunajali.com',
    password='admin123'
)

print("\n" + "="*60)
print("✅ SUPERUSER CREATED SUCCESSFULLY!")
print("="*60)
print(f"Username:  admin")
print(f"Password:  admin123")
print(f"Email:     admin@tunajali.com")
print("="*60 + "\n")
