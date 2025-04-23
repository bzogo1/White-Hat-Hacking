import subprocess
import platform
import re

def get_connected_devices():
    system_os = platform.system()

    if system_os == "Windows":
        command = "arp -a"
    else:  # Linux/macOS
        command = "arp -n"

    result = subprocess.run(command, shell=True, capture_output=True, text=True).stdout

    # Extract IP & MAC addresses
    devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]+)", result)

    print(f"Total devices connected: {len(devices)}\n")
    for ip, mac in devices:
        print(f"IP Address: {ip} | MAC Address: {mac}")

if __name__ == "__main__":
    get_connected_devices()
