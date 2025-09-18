import json
import random
import time
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)

def generate_temperature_data():
    return {
        "sensor_id": str(random.randint(1, 50)),
        "temperature": round(random.uniform(-20.0, 50.0), 2),
        "timestamp": fake.date_time().isoformat()
    }

if __name__ == "__main__":
    topic = 'temperature_sensor_topic'

    while True:
        data = generate_temperature_data()
        key = data['sensor_id']
        producer.send(topic, key=key, value=data)
        print(f"Sent data: {data}")
        time.sleep(2)