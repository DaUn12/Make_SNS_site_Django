FROM python:3.9.0

WORKDIR /home/

RUN echo 'fdgdfgdgg'
# 넣어야지 최신버전으로 가져올 수 있으므로 깃푸시 후 다르게 아무거나 바꿔주기
# 포테이너를 사용하고있어서 발생하는 효과임

RUN git clone https://github.com/DaUn12/lol2.git
    # 깃 주소복붙하여 여기다 옮김

WORKDIR /home/lol2/
    # 깃 이름을 따와야함

RUN echo "SECRET_KEY=django-insecure-6bldunix=$y%a35v0k8!l6&li$76tu8@sp##g3dz2urklk2039" > .env
    # .env 파일에서 따옴

RUN pip install -r requirements.txt
    # 얼린파일을 다시 설치함

RUN pip install gunicorn

# 마리아 디비와 연동이 가능하도록
RUN pip install mysqlclient

EXPOSE 8000

    # 사용할 포트

CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=homepa.settings.deploy && python manage.py migrate --settings=homepa.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=homepa.settings.deploy homepa.wsgi --bind 0.0.0.0:8000"]
# 구니콘, 구니콘에서복붙해논것, 메인파일이름.wsgi, 어떤ip에요청을받을지
