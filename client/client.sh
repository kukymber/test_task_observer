#!/bin/bash

SERVER_URL="http://127.0.0.1:8001/cpu"

while true
do

  CPU_USAGE=$(mpstat 1 1 | awk '/Average/ {print $3}')

  JSON_DATA="{\"cpu\": $CPU_USAGE}"

  curl -X POST -H "Content-Type: application/json" -d "$JSON_DATA" $SERVER_URL

  sleep 10
done
