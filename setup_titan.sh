#!/bin/bash

wget http://s3.thinkaurelius.com/downloads/titan/titan-0.5.0-hadoop2.zip
unzip titan-0.5.0-hadoop2.zip
pushd titan-0.5.0-hadoop2
cp ../rexster-cassandra-es-mogwai.xml conf/rexster-cassandra-es.xml
./bin/titan.sh start
popd

# Wait for Rexster fully start
echo "Waiting for Rexster to fully start..."
sleep 20s

# Setup Sandbox
echo "Setting up Sandbox Indices"
python load_sandbox.py

## Setup GMDB Data
pushd gmdb/data_load
./load_data.sh
popd
