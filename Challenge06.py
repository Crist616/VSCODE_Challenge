#!/usr/bin/python3
#Cristiano Garcia
#16/10/2023

import subprocess

user = subprocess.check_output(["whoami"]).decode().strip()

ip = subprocess.check_output(["ip", "a"]).decode() 

hard = subprocess.check_output(["lshw", "-short"]).decode()

print(user, ip, hard)
