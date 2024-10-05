#!/bin/bash

# install.sh 
#------------------------------------------------------------------
# This script installs boto3 and the schedule module, checking if they are already installed.

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Function for Windows installation
windows_install() {
    echo "Detected Windows (assuming Git Bash)."
    echo "------"

    # Check Python version
    echo "Checking Python version..."
    if command -v python &>/dev/null; then
        python_version=$(python --version)
        echo "Python Version: $python_version"
    else
        handle_error "Python is not installed."
    fi
    echo

    # Check if pip is installed
    echo "Checking if pip is installed..."
    if command -v pip &>/dev/null; then
        echo "pip status: installed."
    else
        handle_error "pip is not installed. Please install pip first."
    fi
    echo

    # Check if pip is working
    echo "Checking if pip is working..."
    if pip --version &>/dev/null; then
        echo "pip status: working (or appears to be...)"
    else
        handle_error "pip is not working."
    fi
    echo

    # Run a one-line Python command
    echo "Checking if Python is working..."
    if python -c "print('Python is working!')" &>/dev/null; then
        echo "Python appears to be working!"
    else
        handle_error "Python command failed."
    fi
    echo "------"

    # List all installed packages
    echo "Listing all installed python packages..."
    pip list || handle_error "Failed to list installed packages."
    echo

    # Check if Python can find installed modules
    echo "Verifying Python can find installed modules..."
    python -c "import sys; print(sys.path)" || handle_error "Failed to retrieve Python module paths."
    echo
    echo "------"

    # Check if boto3 is installed
    echo "Checking if boto3 is installed..."
    if pip show boto3 &>/dev/null; then
        echo "boto3: installed."
    else
        # Install boto3 if not installed
        echo "Installing boto3..."
        pip install boto3 || handle_error "Failed to install boto3."
        echo "boto3 installed successfully."
    fi
    echo

    # Check if schedule is installed
    echo "Checking if schedule is installed..."
    if pip show schedule &>/dev/null; then
        echo "schedule: installed."
    else
        # Install schedule module if not installed
        echo "Installing schedule module..."
        pip install schedule || handle_error "Failed to install schedule."
        echo "schedule installed successfully."
    fi
    echo
    echo "------"
}

# Function for Unix-like (macOS) installation
unix_install() {
    echo "Detected Unix-like OS (assuming macOS or similar)."
    echo "------"

    # Check Python version
    echo "Checking Python version..."
    if command -v python3 &>/dev/null; then
        python_version=$(python3 --version)
        echo "Python Version: $python_version"
    else
        handle_error "Python is not installed."
    fi
    echo

    # Check if pip is installed
    echo "Checking if pip is installed..."
    if command -v pip3 &>/dev/null; then
        echo "pip status: installed."
    else
        handle_error "pip is not installed. Please install pip first."
    fi
    echo

    # Check if pip is working
    echo "Checking if pip is working..."
    if pip3 --version &>/dev/null; then
        echo "pip status: working (or appears to be...)"
    else
        handle_error "pip is not working."
    fi
    echo

    # Run a one-line Python command
    echo "Checking if Python is working..."
    if python3 -c "print('Python is working!')" &>/dev/null; then
        echo "Python appears to be working!"
    else
        handle_error "Python command failed."
    fi
    echo "------"

    # List all installed packages
    echo "Listing all installed python packages..."
    pip3 list || handle_error "Failed to list installed packages."
    echo

    # Check if Python can find installed modules
    echo "Verifying Python can find installed modules..."
    python3 -c "import sys; print(sys.path)" || handle_error "Failed to retrieve Python module paths."
    echo
    echo "------"

    # Check if boto3 is installed
    echo "Checking if boto3 is installed..."
    if pip3 show boto3 &>/dev/null; then
        echo "boto3: installed."
    else
        # Install boto3 if not installed
        echo "Installing boto3..."
        pip3 install boto3 || handle_error "Failed to install boto3."
        echo "boto3 installed successfully."
    fi
    echo

    # Check if schedule is installed
    echo "Checking if schedule is installed..."
    if pip3 show schedule &>/dev/null; then
        echo "schedule: installed."
    else
        # Install schedule module if not installed
        echo "Installing schedule module..."
        pip3 install schedule || handle_error "Failed to install schedule."
        echo "schedule installed successfully."
    fi
    echo
    echo "------"
}

# Main script execution
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    windows_install
else
    unix_install
fi

echo "All checks and installations completed successfully!"
