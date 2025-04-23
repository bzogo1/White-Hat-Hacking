import subprocess
import re

def get_wifi_passwords():
    # Get all saved WiFi profiles
    profiles_data = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout
    profiles = re.findall(r"All User Profile\s*:\s(.*)", profiles_data)

    wifi_passwords = {}

    for profile in profiles:
        # Get password for each WiFi profile
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile.strip(), "key=clear"], capture_output=True, text=True).stdout
        password = re.search(r"Key Content\s*:\s(.*)", profile_info)

        if password:
            wifi_passwords[profile.strip()] = password.group(1)
        else:
            wifi_passwords[profile.strip()] = "No password found"

    return wifi_passwords

# Run the function and display results
passwords = get_wifi_passwords()
for wifi, password in passwords.items():
    print(f"WiFi: {wifi} | Password: {password}")
