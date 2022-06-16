FROM python:3.8.10-alpine

ENV TZ Europe/Moscow
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev \
                          sudo
                          
RUN sudo apt-get install python3-psycopg2

RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install --no-cache-dir -r req.txt

RUN mkdir -p /usr/src/app/
RUN mkdir -p /usr/src/app/static/
WORKDIR /usr/src/app

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
