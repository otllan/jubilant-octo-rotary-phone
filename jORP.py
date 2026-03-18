import time
import os
import socket

cooldown = "10"
software = "C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"

cooldown_seconds = 10

for i in range(cooldown_seconds, 0, -1):
    print(f"cooldown = {i}")
    time.sleep(1)  
print(cooldown)
print("Process complete!")

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:", hostname)
print("Your Computer IP Address is:", IPAddr)
print("deleting os")
print ("os deleted"):  
os.system(f'wmic product where description="{software}" uninstall')
