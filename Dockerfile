FROM ubuntu:20.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y python3-pip python3-dev nodejs npm

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app/static

RUN npm install

WORKDIR /app

RUN mkdir input && mkdir output

EXPOSE 5000/tcp

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]