#FROM python:3.6
FROM ubuntu:18.04

RUN apt update
RUN apt install -y python3

RUN mkdir /var/www

# workdirの指定
# WORKDIR /var/www

# 依存Pythonライブラリインストール
RUN pip install bottle
#RUN pip install uwsgi

# WORKDIR /var/www/src

# CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]

