
#RUN pip install --upgrade pip
#RUN pip install bottle
#RUN pip install uwsgi

#COPY index.py /opt/app
#COPY shikafunc.py /opt/app
#COPY config.ini /opt/app
#COPY test.py /opt/app
#COPY uwsgi.ini /opt/app
#COPY dict /opt/app


FROM python:3.6

RUN mkdir /var/www

# workdirの指定
WORKDIR /var/www

# 依存Pythonライブラリインストール
RUN pip install bottle
RUN pip install uwsgi


WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]

