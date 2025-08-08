import os
import stat
import sys

if getattr(sys, "frozen", False):
	#if ran as .exe
	script_dir = os.path.dirname(sys.executable)
else:
	#if ran as .py
	script_dir = os.path.dirname(os.path.abspath(__file__))

info_file = os.path.join(script_dir, "info.txt")
keys_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "keys"))

if not os.path.exists(keys_dir):
	print(f"Keys folder not found at: {keys_dir}")
	input("Press Enter to exit...")
	sys.exit(1)

print("=== EC2 SSH Setup ===")

key_pair = input("Enter the name of the key pair: ").strip()
ec2_public_dns = input("Enter the EC2 public DNS: ").strip()

key_pair_file = None
for file in os.listdir(keys_dir):
	if file.startswith(key_pair):
		key_pair_file = os.path.join(keys_dir, file)
		break

if not key_pair_file or not os.path.isfile(key_pair_file):
	print(f"Could not find file starting with {key_pair} in {keys_dir}")
	input("Press Enter to exit...")
	sys.exit(1)

try:
	os.chmod(key_pair_file, stat.S_IREAD)
	print(f"\nPermissions set to read-only for: {key_pair_file}")
except Exception as e:
	print(f"\nWarning: Could not set permissions: {e}")

with open(info_file,"w") as f:
	f.write(f"key_pair={key_pair}\n")
	f.write(f"ec2_public_dns={ec2_public_dns}\n")

print("\nSetup complete!")
print(f"info.txt saved in: {info_file}")
print(f"Key file is ready in {keys_dir}")
input("Press Enter to exit...")