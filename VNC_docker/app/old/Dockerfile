From python:3

RUN pip install --upgrade pip
RUN pip install bottle
RUN pip install uwsgi

RUN mkdir /opt/app

COPY index.py /opt/app
COPY shikafunc.py /opt/app
COPY config.ini /opt/app
COPY test.py /opt/app
COPY uwsgi.ini /opt/app
COPY dict /opt/app
