FROM python:3.10.9

EXPOSE 8000

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY myproject/ .
COPY polls/ .

CMD ["manage.py", "runserver", "8000"]