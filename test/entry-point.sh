#!/bin/bash

# entry_point.sh

# Function to determine the OS and set commands for Python and pip
os_check() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "python pip"
    else
        echo "python3 pip3"
    fi
}

# Get Python and pip commands for the shell script
commands=$(os_check)
read -r python_cmd pip_cmd <<< "$commands"

# Run the shell script with the Python and pip commands
./py-check.sh "$python_cmd" "$pip_cmd"
status=$?

# Check if the shell script ran successfully
if [ $status -eq 0 ]; then
    echo "Shell script ran successfully. Now launching boto3-auth-test.py..."

    # Get the same Python command for executing the Python script
    commands=$(os_check)
    read -r python_cmd _ <<< "$commands"  # We only need the Python command here

    $python_cmd boto3-auth-test.py  # Adjust the path if needed
else
    echo "Shell script encountered an error. Exiting."
    exit $status
fi
