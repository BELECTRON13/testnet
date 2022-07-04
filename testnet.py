import time
from colorama import Fore,init
import os
os.system("clear ")

print(Fore.RED+"\nTest Net By BELECTRON ! ")
time.sleep(1)
os.system("apt update && apt upgrade -y ")
os.system("pkg install python ")
os.system("pip install speedtest-cli ")
os.system("clear ")
os.system("speedtest-cli ")
print(Fore.GREEN+"\n------------------ ")
print(Fore.GREEN+"\n< Test-net Done ! > ")
print(Fore.GREEN+"\n------------------ ")
