#!/bin/bash

# Check if KEY_PATH environment variable exists
if [ -z "$KEY_PATH" ]; then
    echo "Error: KEY_PATH environment variable not set."
    exit 5
fi


if [[ -z $private_ip ]];then
  echo "Please provide IP address"
  exit 5
fi

# Private instance details
private_ins="$1"


# New SSH key files
NEW_PRIVATE_KEY="$HOME/new_key.pem"
NEW_PUBLIC_KEY="$HOME/new_key.pem.pub"

# Generate a new SSH key pair
ssh-keygen -t rsa -b 2048 -f "$NEW_PRIVATE_KEY" -N

# Copy the public key to the private instance
scp -i "$KEY_PATH $NEW_PUBLIC_KEY" ubuntu@"$private_ip":~/new_key.pem.pub

# Add the new public key to the authorized_keys file on the private instance
ssh -i "$KEY_PATH" ubuntu@"$private_ip" "cat ~/new_key.pem.pub >> ~/.ssh/authorized_keys && rm ~/new_key.pem.pub"

# Test the new key pair
ssh -i "$NEW_PRIVATE_KEY" ubuntu@"$private_ip" "echo 'Key rotation test successful'"

# Display a message indicating successful key rotation
echo "SSH key rotation and test completed successfully."

exit 0
