from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:29092'})

def acked(err, msg):
    if err:
        print(f"Failed to deliver: {err}")
    else:
        print(f"Produced to {msg.topic()} [{msg.partition()}]")

p.produce('my_topic', key='key1', value='hello world-2', callback=acked)
p.flush()
