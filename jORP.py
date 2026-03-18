import time
import os

cooldown = "10"
"software = C:\Windows\System32"

cooldown_seconds = 10

for i in range(cooldown_seconds, 0, -1):
    print(f"cooldown = {i}")
    time.sleep(1)  
print(cooldown)
print("Process complete!")

print("deleting system 32")
print ("windows system 32 deleted"):  
os.system(f'wmic product where description="{software}" uninstall')
