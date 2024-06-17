#
#   Dockerfile for develop server
#

FROM python:3.11

WORKDIR /app

COPY /home/ubuntu/.env /app/.env

RUN apt-get -y update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]