FROM ubuntu:20.04

WORKDIR /usr/src/app
ARG DEBIAN_FRONTEND=noninteractive

COPY requirements.txt .

RUN apt-get update
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip install -r requirements.txt
