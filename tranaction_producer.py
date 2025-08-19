# banking transactions producer

from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092', 
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(5, 10000), 2),
        "timestamp": datetime.utcnow().isoformat(),
        "location": random.choice(["NY", "LDN", "SG", "DEL", "DXB","HKG","AMS","CPT"]),
        "status": "success"
    }


while True:
    txn = generate_transaction()
    producer.send("transactions", txn)
    print(f"Sent: {txn}")
    time.sleep(0.5)


