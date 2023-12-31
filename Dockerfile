FROM python:3.10-slim

WORKDIR /taskpikasso

ADD ./ /taskpikasso/

RUN apt-get update \
    && apt-get -y install libpq-dev python-dev-is-python3 gcc

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python app/manage.py makemigrations && python app/manage.py migrate && python app/manage.py runserver 0.0.0.0:8000