FROM python:3

WORKDIR /code

ADD . /code

RUN pip install  -r requirements.txt

COPY . .
EXPOSE 8000

CMD python manage.py runserver 0:8000   