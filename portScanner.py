import os

def recon(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")

recon(input("What IP would you like to scan?"))
