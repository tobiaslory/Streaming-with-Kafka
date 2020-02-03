# Streaming with Kafka

#1. See the 3 python files.

#2. See below.

#3. yes

# Kafka Streams

Kafka Streams is a stream-processing framework for processing and analysing data contained in Kafka written in Java.
It was added to the Kafka 0.10.0.0 version.
The library enables the creation of stateful stream-processing applications that are scalable, flexible,
and robust.
The key API is a stream-processing domain-specific language that provides high-level operators such as filter, map,
grouping, windowing, aggregation, joins, and the notion of tables.
In addition, the Processor API can be used to introduce custom operators for a more low-level approach to development.
The DSL and Processor API can be mixed, too.
This draws on critical stream processing principles such as properly distinguishing between event time and processing time, support for windowing, and simple yet effective device state management and real-time querying.
Kafka Streams has a low barrier to entry: You can create and run a small-scale proof-of-concept on a single machine;
and you only need to run additional instances of your program on multiple machines to scale up to high-volume production workloads.
Through exploiting Kafka's parallelism architecture, Kafka Streams transparently performs the load balancing with multiple instances of the same program.

Kafka Streams is buillt as an easy and lightweight client library,
that can be easily integrated into any Java application and is compatible with any current packaging,
installation and run tools that customers have for their streaming applications.
Kafka Streams does not have additional dependencies on structures other than Apache Kafka itself as the internal communications layer.
Kafka Streams supports local fault-tolerant state,
which allows stateful operations suchs as windowed joins and aggregations to be very quick and efficient.
Kafka Streams supports exactly-once processing semantics to ensure that each record is processed once and only once even when there is a failure in the middle of processing on either Streams clients or Kafka brokers.
Kafka Streams utilizes one-record-at-a-time processing to achieve millisecond latency in processing and facilitates event-time-based windowing operations with out-of-order arrival of records.
Kafka Streams offers the necessary primitives for stream processing, along with a high-level Streams DSL and a low-level Processor API.
Kafka Streams uses RocksDB to retain local operator status for stateful stream processing.
Since RocksDB can write to disk, the maintained state may be larger than the main memory that is available.
All updates to local state stores are also written into a topic within the Kafka cluster for fault-tolerance.
It allows for state recreation by reading certain topics and loading all data into RocksDB.
