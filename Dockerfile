FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
#RUN pip install --upgrade pip setuptools wheel
#RUN pip install discord
RUN apk --no-cache add gcc musl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
CMD python Main.py
