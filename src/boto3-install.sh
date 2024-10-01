#!/bin/bash
# boto3-install.sh 

# Check Python version
echo "Checking Python version..."
if command -v python &>/dev/null; then
    python --version
else
    echo "Python is not installed."
    exit 1
fi

# Check if pip is installed
echo "Checking if pip is installed..."
if command -v pip &>/dev/null; then
    echo "pip is installed."
else
    echo "pip is not installed. Please install pip first."
    exit 1
fi

# Check if pip is working
echo "Checking if pip is working..."
if pip --version &>/dev/null; then
    echo "pip is working."
else
    echo "pip is not working."
    exit 1
fi

# Run a one-line Python command
echo "Running a one-line Python command..."
python -c "print('Python is working!')"


# Install boto3
echo "Installing boto3..."
pip install boto3

# Verify if boto3 is installed
echo "Verifying if boto3 is installed..."
if pip show boto3 &>/dev/null; then
    echo "boto3 is successfully installed."
else
    echo "boto3 installation failed."
    exit 1
fi

# List all installed packages
echo "Listing all installed packages..."
pip list

echo "All checks and installations completed successfully!"

