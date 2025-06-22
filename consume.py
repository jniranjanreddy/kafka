from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my_topic'])

while True:
    msg = c.poll(1.0)
    if msg is None: continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Received: {msg.value().decode('utf-8')}")
