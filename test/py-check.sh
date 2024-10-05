#!/bin/bash

# install.sh 
#------------------------------------------------------------------
# This script installs boto3 and the schedule module, checking if they are already installed.

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Function to check AWS CLI configuration
check_aws_cli_config() {
    echo "Checking for AWS CLI configuration..."

    if [[ -f ~/.aws/config ]]; then
        echo "AWS CLI config file found at ~/.aws/config"
        echo "Contents of ~/.aws/config:"
        cat ~/.aws/config
    else
        echo "No AWS CLI config file found at ~/.aws/config."
    fi
    echo

    if [[ -f ~/.aws/credentials ]]; then
        echo "AWS CLI credentials file found at ~/.aws/credentials"
        echo "Verifying contents..."

        key_id=$(awk -F " = " '/aws_access_key_id/ {print $2}' ~/.aws/credentials | tr -d ' ')
        secret_key=$(awk -F " = " '/aws_secret_access_key/ {print $2}' ~/.aws/credentials | tr -d ' ')
        default_region=$(awk -F " = " '/region/ {print $2}' ~/.aws/config | tr -d ' ')
        output_format=$(awk -F " = " '/output/ {print $2}' ~/.aws/config | tr -d ' ')

        [[ -n "$key_id" ]] && echo "AWS Access Key ID: $key_id" || echo "AWS Access Key ID not found."
        [[ -n "$secret_key" ]] && echo "AWS Secret Access Key: $secret_key" || echo "AWS Secret Access Key not found."
        [[ -n "$default_region" ]] && echo "Default Region: $default_region" || echo "Default Region not found."
        [[ -n "$output_format" ]] && echo "Output Format: $output_format" || echo "Output Format not found."
    else
        echo "No AWS CLI credentials file found at ~/.aws/credentials."
    fi
    echo
}

# Function to check if AWS CLI is working
check_aws_cli() {
    echo "Checking if AWS CLI is functioning..."
    if aws ec2 describe-vpcs &>/dev/null; then
        echo "AWS CLI Utility appears to be working."
    else
        echo "AWS CLI Utility is not working. Please check your configuration."
    fi
    echo
}

# Function to check Python version and pip
check_python_and_pip() {
    local python_cmd="$1"
    local pip_cmd="$2"

    echo "Checking Python version..."
    if command -v "$python_cmd" &>/dev/null; then
        echo "$python_cmd Version: $($python_cmd --version)"
    else
        handle_error "$python_cmd is not installed."
    fi
    echo

    echo "Checking if $pip_cmd is installed..."
    if command -v "$pip_cmd" &>/dev/null; then
        echo "$pip_cmd status: installed."
    else
        handle_error "$pip_cmd is not installed. Please install it first."
    fi
    echo

    echo "Checking if $pip_cmd is working..."
    if $pip_cmd --version &>/dev/null; then
        echo "$pip_cmd status: working (or appears to be...)"
    else
        handle_error "$pip_cmd is not working."
    fi
    echo
}

# Function to verify Python functionality
check_python_functionality() {
    local python_cmd="$1"
    echo "Checking if Python is working..."
    if $python_cmd -c "print('Python is working!')" &>/dev/null; then
        echo "Python appears to be working!"
    else
        handle_error "Python command failed."
    fi
    echo
}

# Function to list installed Python packages
list_installed_packages() {
    local pip_cmd="$1"
    echo "Listing all installed python packages..."
    $pip_cmd list || handle_error "Failed to list installed packages."
    echo
}

# Function to check if boto3 and schedule are installed
check_and_install_packages() {
    local pip_cmd="$1"

    for package in boto3 schedule; do
        echo "Checking if $package is installed..."
        if $pip_cmd show "$package" &>/dev/null; then
            echo "$package: installed."
        else
            echo "Installing $package..."
            $pip_cmd install "$package" || handle_error "Failed to install $package."
            echo "$package installed successfully."
        fi
        echo
    done
}

# Main installation function
main() {
    # Get Python and pip commands from arguments
    local python_cmd="$1"
    local pip_cmd="$2"

    # Debugging output
    echo "Using commands: Python = $python_cmd, Pip = $pip_cmd"

    # Check Python and pip
    check_python_and_pip "$python_cmd" "$pip_cmd"

    # Verify Python functionality
    check_python_functionality "$python_cmd"

    # List installed packages
    list_installed_packages "$pip_cmd"

    # Check AWS CLI configuration
    check_aws_cli_config

    # Check if AWS CLI is working
    check_aws_cli

    # Check and install boto3 and schedule
    check_and_install_packages "$pip_cmd"

    echo "All checks and installations completed successfully!"
}

# Execute the main function with arguments
main "$@"
