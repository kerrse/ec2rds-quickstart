import os
import stat
import subprocess
import sys

if getattr(sys, "frozen", False):
	#if ran as .exe
	script_dir = os.path.dirname(sys.executable)
else:
	#if ran as .py
	script_dir = os.path.dirname(os.path.abspath(__file__))
	
info_file = os.path.join(script_dir, "info.txt")
keys_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "keys"))

key_pair = None
ec2_public_dns = None

if not os.path.exists(info_file):
	print("Missing info.txt. Please run install.exe first.")
	input("Press Enter to exit...")
	sys.exit(1)

with open(info_file, "r") as f:
	for line in f:
		if line.startswith("key_pair="):
			key_pair = line.strip().split("=", 1)[1]
		elif line.startswith("ec2_public_dns="):
			ec2_public_dns = line.strip().split("=", 1)[1]

if not key_pair or not ec2_public_dns:
	print("Invalid info.txt. Please run install.exe again.")
	input("Press Enter to exit...")
	sys.exit(1)

key_pair_file = None
for file in os.listdir(keys_dir):
	if file.startswith(key_pair):
		key_pair_file = os.path.join(keys_dir, file)
		break

if not key_pair_file:
	print(f"No key file found for {key_pair} in {keys_dir}. Run install.exe again.")
	input("Press Enter to exit...")
	sys.exit(1)

try:
	os.chmod(key_pair_file, stat.S_IREAD)
except Exception as e: 
	print(f"Could not set permissions: {e}")

ssh_command = ["ssh", "-i", key_pair_file, f"ec2-user@{ec2_public_dns}"]

try:
	subprocess.run(ssh_command)
except FileNotFoundError:
	print("SSH not found. Install OpenSSH and add it to PATH.")