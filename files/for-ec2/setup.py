import os

info_file = "info.txt"
inc_file = "dbinfo.inc"

db_instance_endpoint = None
master_password = None

#in the event that info.txt already exists
if os.path.exists(info_file):
    with open(info_file, "r") as file_obj:
        for line in file_obj:
            if "db_instance_endpoint" in line:
                db_instance_endpoint = line.strip().split("=", 1)[1]
            elif "master_password" in line:
                master_password = line.strip().split("=", 1)[1]

if not db_instance_endpoint:
    db_instance_endpoint = input("Enter the DB instance endpoint: ").strip()

if not master_password:
    master_password = input("Enter the master password: ").strip()

#start writing to info.txt
with open(info_file, "a") as file_obj:
    if not os.path.exists(info_file) or "db_instance_endpoint=" not in open(info_file).read():
        file_obj.write(f"db_instance_endpoint={db_instance_endpoint}\n")
    if not os.path.exists(info_file) or "master_password=" not in open(info_file).read():
        file_obj.write(f"master_password={master_password}\n")

print("info.txt updated")

#start writing to dbinfo.inc
with open(inc_file, "w") as file_obj:
    file_obj.write(f"""<?php
    define('DB_SERVER', '{db_instance_endpoint}');
    define('DB_USERNAME', 'admin');
    define('DB_PASSWORD', '{master_password}');
    define('DB_DATABASE', 'sample');\n?>""")

print("dbinfo.inc updated")




