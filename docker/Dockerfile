FROM debian:bullseye

WORKDIR /usr/bin/

RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata default-jdk
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y keyboard-configuration
RUN apt-get install -y git devscripts config-package-dev debhelper-compat wget

RUN apt-get install -y bindgen  build-essential clang libasound2-dev libcap-dev libgbm-dev libvirglrenderer-dev    libwayland-bin  libwayland-dev pkg-config protobuf-compiler python wayland-protocols tmux

WORKDIR /opt
RUN wget https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
RUN tar -xzf kafka_2.13-3.1.0.tgz


WORKDIR /opt/kafka_2.13-3.1.0

COPY ./setup_inside_docker.sh /opt/kafka_2.13-3.1.0/setup_inside_docker.sh

CMD bash #"sh /opt/kafka_2.13-3.1.0/setup_inside_docker.sh" # bash #bin/kafka-server-start.sh config/server.properties
