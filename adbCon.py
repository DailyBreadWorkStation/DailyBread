import subprocess

def connect():
    """
    Connects to android devices on the network; add the static ip address into adb_ip_list
    """
    adb_ip_list = ["10.0.0.12"]
    for ip in adb_ip_list:
        subprocess.call(f"adb connect {ip}:5555", shell=True)
