#FROM ubuntu:20.04
#FROM debian:stable
FROM debian:bullseye

WORKDIR /usr/bin/

RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata default-jdk
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y keyboard-configuration
RUN apt install -y git devscripts config-package-dev debhelper-compat wget

RUN apt install -y bindgen  build-essential clang libasound2-dev libcap-dev libgbm-dev libvirglrenderer-dev    libwayland-bin  libwayland-dev pkg-config protobuf-compiler python wayland-protocols tmux

WORKDIR /opt
RUN wget https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
RUN tar -xzf kafka_2.13-3.1.0.tgz

# RUN wget https://dlcdn.apache.org/zookeeper/zookeeper-3.7.0/apache-zookeeper-3.7.0-bin.tar.gz
# RUN tar -zxf apache-zookeeper-3.7.0-bin.tar.gz

WORKDIR /opt/kafka_2.13-3.1.0

COPY ./setup_insider_docker.sh /opt/kafka_2.13-3.1.0/setup_insider_docker.sh

CMD bash # bin/kafka-server-start.sh config/server.properties
