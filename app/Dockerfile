FROM python:3.10.9-buster

WORKDIR /app
RUN apt-get update




# Instalacion de paquetes

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY main.py main.py
COPY src src
COPY config config


EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
