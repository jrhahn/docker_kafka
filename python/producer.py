from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewPartitions
from kafka.errors import InvalidPartitionsError

import shared


def run():
    admin_client = KafkaAdminClient(bootstrap_servers=shared.bootstrap_servers)

    topic_partitions = {
        shared.topic: NewPartitions(total_count=int(shared.num_partitions))
    }

    try:
        admin_client.create_partitions(topic_partitions)
    except InvalidPartitionsError:
        print("partition probably exists.")

    producer = KafkaProducer(bootstrap_servers=shared.bootstrap_servers)

    for ii in range(1000):
        producer.send(
            topic='grid_search',
            value=f'settings_{ii}'.encode(encoding="UTF8"),
            partition=int(ii % shared.num_partitions)
        )

    print("")


if __name__ == '__main__':
    run()
