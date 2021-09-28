from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/'+ secret_name)   # 경로에있는 시크릿키를 읽을 수 있음
    secret = file.read()
    secret = secret.lstrip().rstrip()   # 좌우 공백제거
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
    # False 시 어디서 틀렷는지 알수 없게함  ( 배포할때 false 로함)
    # 개발 시 True 로함

ALLOWED_HOSTS = ["*"]       # 모든 호스트를 허용


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}