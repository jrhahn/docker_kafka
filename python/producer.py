from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewPartitions, NewTopic
from kafka.errors import InvalidPartitionsError, TopicAlreadyExistsError

import shared


def run():
    admin_client = KafkaAdminClient(bootstrap_servers=shared.bootstrap_servers)

    try:
        admin_client.create_topics([
            NewTopic(
                name=shared.topic,
                num_partitions=shared.num_partitions,
                replication_factor=1)
        ])
    except TopicAlreadyExistsError:
        # topic already exists
        pass

    producer = KafkaProducer(bootstrap_servers=shared.bootstrap_servers)

    for ii in range(10000):
        print(f"Sending {ii}")

        producer.send(
            topic=shared.topic,
            value=f'settings_{ii}'.encode(encoding="UTF8")
        )

    producer.flush()

    print("Done.")


if __name__ == '__main__':
    run()
