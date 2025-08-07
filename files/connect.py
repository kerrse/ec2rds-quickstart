import os

info_file = "info.txt"

key_pair = None
ec2_public_dns = None

if os.path.exists(info_file):
    with open(info_file, "r") as file_obj:
        for line in file_obj:
            if "key_pair" in line:
                key_pair = line.strip().split("=", 1)[1]
            elif "ec2_public_dns" in line:
                ec2_public_dns = line.strip().split("=", 1)[1]

if not key_pair:
    key_pair = input("Enter the name of the key pair: ").strip()

if not ec2_public_dns:
    ec2_public_dns = input("Enter the EC2 public DNS: ").strip()

with open(info_file, "a") as file_obj:
    if not os.path.exists(info_file) or "key_pair=" not in open(info_file).read():
        file_obj.write(f"key_pair={key_pair}\n")
        print(f"Key pair set to: {key_pair}\n")
    if not os.path.exists(info_file) or "ec2_public_dns=" not in open(info_file).read():
        file_obj.write(f"ec2_public_dns={ec2_public_dns}\n")
        print(f"EC2 public DNS set to: {ec2_public_dns}\n")

print("info.txt updated")
