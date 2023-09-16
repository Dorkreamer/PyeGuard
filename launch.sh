#!/bin/bash

# Name of your virtual environment
venv_name=".venv"

# Function to create and activate the virtual environment
create_and_activate_venv() {
    if [ ! -d "$venv_name" ]; then
        echo "Creating virtual environment '$venv_name'..."
        python -m venv "$venv_name"
    fi

    # Activate the virtual environment
    source "$venv_name/bin/activate"

    # Install necessary modules
    pip install -r requirements.txt
}

# Function to run the Python script and handle errors
run_python_script() {
    python -OO main.py
    exit_status=$?  # Get the exit status of the Python script

    if [ $exit_status -ne 0 ]; then
        echo "Python script exited with an error. Relaunching..."
    else
        echo "Python script exited normally."
    fi
}

# Create and activate the virtual environment
create_and_activate_venv

# Run the Python script in a loop
while true; do
    run_python_script
done

# Deactivate the virtual environment when done
deactivate
