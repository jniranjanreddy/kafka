## https://www.youtube.com/watch?v=B7CwU_tNYIE
# kafka
## https://www.youtube.com/watch?v=AyjdQrS7c9o
## https://github.com/pedrojunqueira/PytalistaYT/tree/master/Python/kafka
## https://github.com/Azure/azure-event-hubs-for-kafka/blob/master/quickstart/python/setup.sh


## Create topic
```
docker exec -it kafka kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
## Produce mesage
```
docker exec -it kafka kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```

## Consume Message
```
docker exec -it kafka kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```

```
docker volume ls
docker run -it --rm -v zookeeper-data:/data busybox ls /data
```
## Kafdrop
```
docker run -d -p 7000:9000 \
    -e KAFKA_BROKERCONNECT=<kafkaip>:9092 \
    -e SERVER_SERVLET_CONTEXTPATH="/" \
    obsidiandynamics/kafdrop
```
```
Kafka Interview Questions and Answers
🟢 Basic Level
1. What is Apache Kafka?

Answer:
Apache Kafka is a distributed event streaming platform used to build real-time data pipelines and streaming applications.
It allows publishing, storing, and subscribing to streams of records in a fault-tolerant and scalable manner.

2. What are the key components of Kafka?

Answer:

Producer: Sends messages to Kafka topics.

Consumer: Reads messages from topics.

Broker: Kafka server that stores and serves data.

Topic: Logical channel where messages are published.

Partition: Subdivision of a topic for parallelism.

Zookeeper / KRaft: Manages cluster metadata (KRaft replaces Zookeeper in newer versions).

3. What is a Kafka topic?

Answer:
A topic is a logical stream where records are published. It’s partitioned and replicated across brokers for scalability and reliability.

4. What is a Kafka partition and why is it important?

Answer:
Each topic is split into partitions, enabling parallel reads/writes.
Partitions also define ordering — messages within a partition are ordered, but not across partitions.

5. What is an offset in Kafka?

Answer:
An offset is a unique ID assigned to each message within a partition, indicating its position. Consumers use offsets to track progress.

6. What is a consumer group?

Answer:
A consumer group is a collection of consumers working together to consume messages from one or more topics — each partition is consumed by only one consumer in the group.

7. What is a Kafka broker?

Answer:
A broker is a Kafka server that hosts topics and handles data replication, storage, and client requests.
A Kafka cluster can have multiple brokers.

8. What happens when a Kafka broker fails?

Answer:

Partition leadership shifts to another replica.

Kafka ensures high availability through replication.

Producers and consumers automatically reconnect.

9. What is replication in Kafka?

Answer:
Each partition is replicated across multiple brokers (replication factor).
One replica is the leader, others are followers.

10. How does Kafka ensure durability?

Answer:

Messages are written to disk (commit log).

Replicated across brokers.

Acknowledgments (acks=all) ensure durability before success is confirmed.

⚙️ Intermediate Level
11. Difference between Kafka and RabbitMQ?
Feature	Kafka	RabbitMQ
Model	Pub/Sub (log-based)	Message Queue
Ordering	Partition level	Not guaranteed
Throughput	Very high	Moderate
Use Case	Streaming, event-driven	Work queues, RPC
12. How do you ensure message ordering in Kafka?

Answer:
Use the same key for related messages so they go to the same partition.

13. Explain Kafka retention policy.

Answer:
Kafka retains messages for a specified duration or until a size limit is reached (default: 7 days).
Set via:

log.retention.hours=168
log.retention.bytes=1073741824

14. What is idempotent producer in Kafka?

Answer:
An idempotent producer ensures that duplicate messages are not written in case of retries or network errors (enable.idempotence=true).

15. What is a Kafka offset commit?

Answer:
Consumers commit offsets to record progress.

Auto commit: Kafka handles it periodically.

Manual commit: Application commits explicitly after processing.

16. How does Kafka handle backpressure?

Answer:
By controlling batch sizes, consumer lag monitoring, and applying producer rate limits (max.in.flight.requests.per.connection, linger.ms, etc.).

17. What is Kafka Streams?

Answer:
A Java library to process and transform data within Kafka — allows joining, filtering, aggregations on event streams.

18. How is Kafka monitored?

Answer:

Metrics exporters: JMX Exporter → Prometheus → Grafana

Tools: Confluent Control Center, Kafka UI, Kafdrop, Burrow

☸️ Kafka on Kubernetes
19. How do you deploy Kafka in Kubernetes?

Answer:
Using Helm charts or Operators:

Strimzi Operator (most popular)

Bitnami Helm chart

Confluent Operator

20. What is Strimzi?

Answer:
Strimzi is a Kubernetes Operator for running Apache Kafka. It automates:

Kafka cluster setup

Zookeeper or KRaft configuration

Scaling, rolling updates

TLS and authentication via cert-manager

User and topic management

21. What are key CRDs in Strimzi Kafka operator?

Answer:

Kafka – defines cluster configuration

KafkaTopic – manages topics

KafkaUser – manages users

KafkaConnector – for Connect

KafkaMirrorMaker – for mirroring clusters

22. How can you enable TLS in Kafka on Kubernetes?

Answer:
Strimzi integrates with cert-manager to auto-issue TLS certificates:

listeners:
  tls:
    authentication:
      type: tls

23. How to expose Kafka outside the Kubernetes cluster?

Answer:

Use LoadBalancer type listener.

Or use NodePort or Ingress + Nginx with TLS.
Example:

listeners:
  external:
    type: loadbalancer

24. How do you scale Kafka brokers on Kubernetes?

Answer:
Update the Kafka CRD:

spec:
  kafka:
    replicas: 5


Strimzi handles rolling update and rebalancing.

25. How to persist Kafka data in Kubernetes?

Answer:
Use PersistentVolumeClaims (PVCs):

storage:
  type: persistent-claim
  size: 100Gi

🚨 Advanced and Troubleshooting
26. What happens if a Kafka broker loses its data?

Answer:

If replicas exist → Kafka re-replicates data.

If the lost broker was the leader → new leader is elected from in-sync replicas (ISR).

If no ISR → possible data loss depending on acks settings.

27. How to achieve zero data loss in Kafka?

Answer:

acks=all

min.insync.replicas >= 2

replication.factor >= 3

Idempotent producers

Durable storage (SSD/Persistent Disks)

28. What is ISR (In-Sync Replicas)?

Answer:
ISR is the set of replicas that are fully caught up with the leader.
Kafka only commits messages when all ISR replicas have acknowledged.

29. How do you detect consumer lag?

Answer:
Use metrics like consumer_lag from JMX exporter or Kafka UI tools (Burrow, Prometheus dashboards).

30. How can you integrate Kafka with monitoring tools?

Answer:

JMX Exporter → Prometheus → Grafana

Loki/Fluent Bit for log aggregation

Azure Monitor / Datadog / Elastic Stack

31. How to restart Kafka broker pods in Kubernetes safely?

Answer:
Use rolling update strategy in the Kafka CRD.
Strimzi ensures one broker is restarted at a time while maintaining quorum.

32. How do you configure Kafka authentication and authorization?

Answer:

SASL/PLAIN, SASL/SCRAM, mTLS supported.

Strimzi example:

authentication:
  type: scram-sha-512
authorization:
  type: simple

33. What are Kafka Connect and MirrorMaker?

Answer:

Kafka Connect: For integrating Kafka with external systems (DBs, storage).

MirrorMaker: For replicating topics between clusters (disaster recovery / multi-region setup).

34. How do you handle Kafka upgrade in Kubernetes?

Answer:
Strimzi manages rolling upgrades:

Update image version in Kafka CRD.

Operator upgrades one broker at a time, ensuring ISR availability.

35. How do you back up and restore Kafka topics?

Answer:

MirrorMaker replication to another cluster.

Snapshot PVCs at storage layer (Azure Disk / EBS).

Use tools like Kafka Exporter to dump messages.

🧠 Scenario-Based
36. Your Kafka consumers are lagging. What do you check?

Answer:

Consumer lag metrics (Prometheus/Grafana).

Consumer group health.

Broker load / network latency.

Partitions rebalancing.

Increase consumers or partition count.

37. Kafka broker pod is CrashLooping — what to check?

Answer:

PVC mount or volume corruption.

Zookeeper/KRaft connectivity.

Broker ID conflicts.

Check logs for OutOfMemoryError, BindException, or InvalidReplicationFactor.

38. Kafka messages not delivered to consumers.

Answer:

Check topic existence and partition count.

Verify offsets and lag.

Ensure correct consumer group.

Check ACLs and authentication.

39. Kafka broker storage is full. What happens?

Answer:

Producers get KafkaStorageException.

Topic compaction or retention cleanup may free space.

Increase storage or move data.

40. Explain Kafka in the context of microservices.

Answer:
Kafka acts as the event backbone — microservices communicate asynchronously via topics, enabling decoupled, scalable architectures.

✅ Bonus: Tools you should mention in interviews

Strimzi Operator / Confluent Operator

Kafka UI (Provectus)

Kafdrop

Burrow (consumer lag monitoring)

Kafka Exporter (Prometheus)

Fluent Bit + Loki / Elastic Stack
```
