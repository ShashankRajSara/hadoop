# Start ZOOKEEPER and KAFKA
cd $KAFKA_HOME/bin
sudo ./zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &	=> Starts Zookeeper and runs in background
sudo ./kafka-server-start.sh $KAFKA_HOME/config/server.properties &			=> Starts Kafka and runs in background

# Verify KAFKA Startup
sudo netstat -tulpen | grep 2181		=> Zookeeper default port
sudo netstat -tulpen | grep 9092		=> Kafka broker default port

# Stop ZOOKEEPER and KAFKA
cd $KAFKA_HOME/bin
sudo ./kafka-server-stop.sh			=> Stops Kafka
sudo ./zookeeper-server-stop.sh		=> Stops Zookeeper

# Navigate to KAFKA HOME directory
cd $KAFKA_HOME

## Kafka Commands

#Create Topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

#List Topics
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

#Describe Topic
bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test

#Produce Message
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

#Consume Message (from current subscription)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test

#Consume Message (from beginning)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

#Consume Message (with consumer group)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --group test-group

#Consume Message (from specific partition)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --partition 0 --offset earliest

#Consume Message (from specific offset)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --partition 0 --offset 3

#Alter Topic
bin/kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic test --partitions 3

#Delete Topic
bin/kafka-topics.sh --delete --bootstrap-server localhost:2181 --topic test

#Consumer Groups
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group test-group
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups






###########ALTERNATIVE APPROACH: Package Installation##########

#Install Kafka packages
sudo apt-get install kafka
sudo apt-get install kafka-server

#Ensure broker id is unique for every node and zookeeper.connect property points to right one
sudo vi /etc/kafka/conf/server.properties

#Start Kafka service
sudo service kafka-server start

#Verify Kafka installation
zookeeper-client
ls /brokers/ids
get /brokers/ids/<ID>

###############################################################