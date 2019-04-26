FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-bancos
WORKDIR /django-bancos
ADD requirements.txt /django-bancos/
RUN pip install -r requirements.txt
ADD . /django-bancos/
RUN apt-get update && apt-get -y install postgresql

