from kafka import KafkaConsumer
import os

BROKERS = os.getenv("KAFKA_BROKER", "localhost:9092")
TOPIC = os.getenv("TOPIC", "topico")
GROUP_ID = os.getenv("GROUP_ID", "python-consumer-group")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKERS.split(","),
    group_id=GROUP_ID,
    auto_offset_reset="earliest"
)

print(f"Consuming messages from topic '{TOPIC}'...")

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
