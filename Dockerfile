FROM alpine:3.17

RUN apk add --no-cache python3-dev py3-pip && \
    pip3 install --upgrade pip && \
    apk add --no-cache mysql-client

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENV MYSQL_DATABASE=<adso>
ENV MYSQL_USER=<root>
ENV MYSQL_HOST=<host>

CMD ["python3", "app.py"]