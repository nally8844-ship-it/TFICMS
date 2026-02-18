from accounts.models import User
User.objects.create_superuser(email='admin@tficms.com', username='admin', password='admin', role='superadmin')