#!/bin/bash

#connect.sh - setting permissions for key pairs and creating an ssh shortcut

info_file="$(dirname "$0")/info.txt"
keys_dir="$(dirname "$0")/../keys"
key_pair=""
ec2_public_dns=""

while IFS='=' read -r key value; do
    case "$key" in
        key_pair) key_pair="$value" ;;
        ec2_public_dns) ec2_public_dns="$value" ;;
    esac
done < "$info_file"

if [ -z "$key_pair" ] || [ -z "$ec2_public_dns" ]; then
    echo "Missing key_pair or ec2_public_dns in $info_file"
    echo "Please run setup.py to create info.txt"
    exit 1
fi

key_pair_extension=$(find "$keys_dir" -type f -name "${key_pair}*" | head -n 1)

if [ -z "$key_pair_extension" ] || [ ! -f "$key_pair_extension" ]; then
    echo "Could not find key pair file matching $key_pair in $keys_dir"
    echo "Please ensure the key pair file exists in the keys directory"
    exit 1
fi

#setting permissions for $key_pair_extension
#owner can read but no permissions for anybody else
#otherwise it will return "permissions for $key_pair_extension are too open"
current_permissions=$(stat -c "%a" "$key_pair_extension")

if [ "$current_permissions" != "400" ]; then
    echo "Permissions for $key_pair_extension are currently $current_permissions"
    echo "Setting permissions for $key_pair_extension to 400"
    chmod 0400 "$key_pair_extension"
else
    echo "Hooray! Permissions for $key_pair_extension are already set to 400!"
fi

#automated ssh connection to EC2 instance
ssh -i "$key_pair_extension" ec2-user@"$ec2_public_dns"