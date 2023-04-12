FROM alpine:3.17

RUN apk add --no-cache python3-dev py3-pip && \
    pip3 install --upgrade pip && \
    apk add --no-cache mariadb-connector-c-dev build-base

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install --force-reinstall --ignore-installed six -r requirements.txt
RUN pip install mysqlclient

EXPOSE 5000

ENV MYSQL_DATABASE="adso"
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD=""
ENV MYSQL_HOST="localhost"

CMD ["python3", "app.py"]