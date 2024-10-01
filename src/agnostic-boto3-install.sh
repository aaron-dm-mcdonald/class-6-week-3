#!/bin/bash

# install.sh 

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Function for Windows installation
windows_install() {
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
}

# Function for Unix-like (macOS) installation
unix_install() {
    # Check Python version
    echo "Checking Python version..."
    if command -v python3 &>/dev/null; then
        python3 --version
    else
        handle_error "Python is not installed."
    fi

    # Check if pip is installed
    echo "Checking if pip is installed..."
    if command -v pip3 &>/dev/null; then
        echo "pip is installed."
    else
        handle_error "pip is not installed. Please install pip first."
    fi

    # Check if pip is working
    echo "Checking if pip is working..."
    if pip3 --version &>/dev/null; then
        echo "pip is working."
    else
        handle_error "pip is not working."
    fi

    # Run a one-line Python command
    echo "Running a one-line Python command..."
    python3 -c "print('Python is working!')" || handle_error "Python command failed."

    # List all installed packages
    echo "Listing all installed packages..."
    pip3 list || handle_error "Failed to list installed packages."

    # Check if Python can find installed modules
    echo "Verifying Python can find installed modules..."
    python3 -c "import sys; print(sys.path)" || handle_error "Failed to retrieve Python module paths."

    # Install boto3
    echo "Installing boto3..."
    pip3 install boto3 || handle_error "Failed to install boto3."

    # Verify if boto3 is installed
    echo "Verifying if boto3 is installed..."
    if pip3 show boto3 &>/dev/null; then
        echo "boto3 is successfully installed."
    else
        handle_error "boto3 installation failed."
    fi
}

# Main script execution
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows (Git Bash)."
    windows_install
else
    echo "Detected Unix-like OS (macOS or similar)."
    unix_install
fi

echo "All checks and installations completed successfully!"
