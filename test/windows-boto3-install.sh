#!/bin/bash

# windows-install-boto3.sh 

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Check Python version
echo "Checking Python version..."
if command -v python &>/dev/null; then
    python --version
else
    handle_error "Python is not installed."
fi

# Check if pip is installed
echo "Checking if pip is installed..."
if command -v pip &>/dev/null; then
    echo "pip is installed."
else
    handle_error "pip is not installed. Please install pip first."
fi

# Check if pip is working
echo "Checking if pip is working..."
if pip --version &>/dev/null; then
    echo "pip is working."
else
    handle_error "pip is not working."
fi

# Run a one-line Python command
echo "Running a one-line Python command..."
python -c "print('Python is working!')" || handle_error "Python command failed."

# List all installed packages
echo "Listing all installed packages..."
pip list || handle_error "Failed to list installed packages."

# Check if Python can find installed modules
echo "Verifying Python can find installed modules..."
python -c "import sys; print(sys.path)" || handle_error "Failed to retrieve Python module paths."

# Install boto3
echo "Installing boto3..."
pip install boto3 || handle_error "Failed to install boto3."

# Verify if boto3 is installed
echo "Verifying if boto3 is installed..."
if pip show boto3 &>/dev/null; then
    echo "boto3 is successfully installed."
else
    handle_error "boto3 installation failed."
fi

echo "All checks and installations completed successfully!"
