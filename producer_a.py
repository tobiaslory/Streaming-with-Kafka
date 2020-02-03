import random
import time

from kafka import KafkaProducer

if __name__ == '__main__':
    kafka_producer = KafkaProducer()
    while True:
        kafka_producer.send(topic='numbers', key=bytes('A', "utf-8"), value=bytes([random.randrange(0, 10, 2)]))
        time.sleep(1)
