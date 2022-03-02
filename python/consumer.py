import argparse

from kafka import KafkaConsumer, TopicPartition

import shared


def run(
    do_manually_assign_to_partition: bool = False,
    partition_id: int = 0
) -> None:
    consumer = KafkaConsumer(
        shared.topic,
        bootstrap_servers=shared.bootstrap_servers,
        group_id=shared.group_id
    )

    if do_manually_assign_to_partition:
        consumer.assign([TopicPartition(shared.topic, partition=partition_id)])

    for msg in consumer:
        print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List fish in aquarium.")
    parser.add_argument("-p", "--partition_id", type=int, default=0)
    args = parser.parse_args()

    run(partition_id=args.partition_id)
