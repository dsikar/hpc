#!/bin/bash

while true; do
    ./daily_job.sh
    sleep $((24 * 60 * 60))  # Sleep for 24 hours (in seconds)
done
