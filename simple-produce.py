from confluent_kafka import Producer

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
}

# Create Producer instance
producer = Producer(conf)

def delivery_report(err, msg):
    """Callback for message delivery report."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Kafka topic
topic = 'test_topic'  # Replace with your topic name

# Message to send
message = 'Hello, Kafka!'

# Send message
producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered
producer.flush()

print("Message sent successfully!")

