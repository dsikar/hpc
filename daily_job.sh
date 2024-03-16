#!/bin/bash

# Get the current timestamp
timestamp=$(date +%Y%m%d%H%M%S)

# Run the squeue command and save the output to log_file.txt
squeue > log_file.txt

# Run the Python script and redirect the output to a file with the timestamp
python3 claude_parser.py > processed_log_${timestamp}.txt
