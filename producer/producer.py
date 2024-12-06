from kafka import KafkaProducer
import os
import time

BROKERS = os.getenv("KAFKA_BROKER", "localhost:9092")
TOPIC = os.getenv("TOPIC", "topico")

producer = KafkaProducer(bootstrap_servers=BROKERS)

try:
    print(f"Producing messages to topic '{TOPIC}'...")
    for i in range(1, 11):
        message = f"Message {i}"
        producer.send(TOPIC, value=message.encode('utf-8'))
        print(f"Sent: {message}")
        time.sleep(1)
finally:
    producer.close()
