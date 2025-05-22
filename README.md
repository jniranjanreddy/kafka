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
