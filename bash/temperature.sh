#!/bin/bash

printf "%-15s%5s\n" "TIMESTAMP" "TEMP(degC)"
printf "%20s\n" "--------------------"

if ! echo $1 | egrep -q '^[0-9]+$' ; then
    echo "Specify the timeout time, e.g.: temperature.sh <number>" >&2
    exit 1
fi

while true; do
    temp=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
    timestamp=$(date +'%s')
    printf "%-15s%5s\n" "$timestamp" "$temp"
    sleep $1
done
