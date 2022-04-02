from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "multi",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
    )

    for msg in consumer:
        print("registered user = {}".format(json.loads(msg.value)))