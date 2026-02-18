from pathlib import Path
import environ, os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env.bool('DEBUG')
SECRET_KEY = env('SECRET_KEY', default='temporary-secret-key-123456')
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '*'
]

INSTALLED_APPS = [
    # Admin interface theme - MUST be before django.contrib.admin
    'admin_interface',
    'colorfield',
    
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'accounts',
    'patients',
    'appointments',
    'emr',
    'fertility_unit',
    'ivf',
    'andrology_lab',
    'embryology_lab',
    'ultrasound',
    'nursing',
    'pharmacy',
    'billing',
    'cryobank',
    'counseling',
    'inventory',
    'hr_payroll',
    'notifications',
    'reports',
    'audit',
    'compliance',
    'dashboard',

    # Third-party packages
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
    'drf_yasg',
    'import_export',
]

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tfirms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tfirms.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_DATABASE'),
        'USER': env('SQL_USER'),
        'PASSWORD': env('SQL_PASSWORD'),
        'HOST': env('SQL_HOST'),
        'PORT': env('SQL_PORT'),
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CELERY_BROKER_URL = env('CELERY_BROKER')
CELERY_RESULT_BACKEND = env('CELERY_BROKER')