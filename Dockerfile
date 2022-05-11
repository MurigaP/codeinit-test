FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv

RUN mkdir /src
WORKDIR /src     

RUN pip install pipenv
COPY Pipfile Pipfile.lock /src/
RUN pip install pipenv && pipenv install --system

COPY . /src/