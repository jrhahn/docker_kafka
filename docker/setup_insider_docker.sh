#!/bin/bash


cd /opt/kafka_2.13-3.1.0

IP=$(hostname -I | awk '{print $1}')
echo $IP
echo "listeners=PLAINTEXT://$IP:9092" >> config/server.properties 
echo "advertised.listeners=PLAINTEXT://10.67.1.138:9092" >> config/server.properties

sh bin/zookeeper-server-start.sh config/zookeeper.properties &
sh bin/kafka-server-start.sh config/server.properties &
