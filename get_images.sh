#!/bin/bash

docker pull dockerfile/elasticsearch &
docker pull poklet/cassandra &
docker pull apobbati/titan-rexster &
wait %1 %2 %3

