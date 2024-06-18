FROM python:3.11

WORKDIR /app

COPY . .

RUN apt-get -y update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "unix:/tmp/gunicorn.sock" ,"config.wsgi:application"]
