Start the Redpanda cluster

- docker-compose -f redpanda/docker-compose up -d

Know the version of redpanda
- docker exec redpanda-1 rpk version
v22.3.5 (rev 28b2443)

Create a topic
- docker exec redpanda-1 rpk topic create test-topic
TOPIC       STATUS
test-topic  OK


Connecting with kafka-server

pip install kafka-python