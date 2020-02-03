from kafka import KafkaConsumer

if __name__ == '__main__':
    kafka_consumer = KafkaConsumer('numbers')
    for msg in kafka_consumer:
        print(msg.key.decode("utf-8"), int.from_bytes(msg.value, byteorder='big'))