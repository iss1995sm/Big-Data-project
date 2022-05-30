# INSTALL
- https://www.youtube.com/watch?v=4xFZ_iTZLTs

    - docker-compose -f docker-compose.yml up -d

    - docker exec -it kafka /bin/sh


# Topics
- /opt/kafka_<version>/bin:

    - kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic

    - kafka-topics.sh --list --zookeeper zookeeper:2181

    - kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic messages

    - kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic messages

    - kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic first_kafka_topic

# Producer
- /opt/kafka_<version>/bin:
    - kafka-console-producer.sh --broker-list kafka:9092 --topic messages


# Consumer
- /opt/kafka_<version>/bin:
    - kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages