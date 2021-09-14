from .base import *
    # base 에있는 모든 걸 가져옴


env_list =dict()
local_env = open(os.path.join(BASE_DIR, '.env'), encoding='utf-8')      #os.path.join : os의 경로(settings의 파일과 .env 파일의 경로)를 합침

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n','')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z!wute_#a%5cmq6lu^6=33e^)=6zq)cuv3l_vasd4ja!2ow288'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
    # False 시 어디서 틀렷는지 알수 없게함  ( 배포할때 false 로함)
    # 개발 시 True 로함

ALLOWED_HOSTS = ["*"]       # 모든 호스트를 허용

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
