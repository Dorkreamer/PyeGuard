#!/bin/bash

while true; do
    source .venv/bin/activate
    python -OO main.py
    exit_status=$?  # Get the exit status of the Python script
    
    # Check if the exit status is non-zero (indicating an error)
    if [ $exit_status -ne 0 ]; then
        echo "Python script exited with an error. Relaunching..."
    else
        echo "Python script exited normally."
        break  # Exit the loop if the script exited without error
    fi
done
