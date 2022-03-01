import argparse

from kafka import KafkaConsumer, TopicPartition

import shared


def run(partition_id):
    consumer = KafkaConsumer(
        bootstrap_servers=shared.bootstrap_servers,
        auto_offset_reset='latest'
    )
    consumer.assign([TopicPartition(shared.topic, partition=partition_id)])

    for msg in consumer:
        print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List fish in aquarium.")
    parser.add_argument("-p", "--partition_id", type=int, default=0)
    args = parser.parse_args()

    run(partition_id=args.partition_id)
