#!/usr/bin/env/python
import os
import sys ,shutil ,time
from time import sleep
os.system("clear")

logo = """
╭━╮╭━┳━━━┳━━━╮      ╭━━━┳╮╱╭┳━━━┳━╮╱╭┳━━━┳━━━┳━━━╮
┃┃╰╯┃┃╭━╮┃╭━╮┃      ┃╭━╮┃┃╱┃┃╭━╮┃┃╰╮┃┃╭━╮┃╭━━┫╭━╮┃
┃╭╮╭╮┃┃╱┃┃┃╱╰╯ <==> ┃┃╱╰┫╰━╯┃┃╱┃┃╭╮╰╯┃┃╱╰┫╰━━┫╰━╯┃
┃┃┃┃┃┃╰━╯┃┃╱╭╮ <==> ┃┃╱╭┫╭━╮┃╰━╯┃┃╰╮┃┃┃╭━┫╭━━┫╭╮╭╯
┃┃┃┃┃┃╭━╮┃╰━╯┃      ┃╰━╯┃┃╱┃┃╭━╮┃┃╱┃┃┃╰┻━┃╰━━┫┃┃╰╮
╰╯╰╯╰┻╯╱╰┻━━━╯      ╰━━━┻╯╱╰┻╯╱╰┻╯╱╰━┻━━━┻━━━┻╯╰━╯"""
print(logo)
print("")
x = """=====>>>>>>>   𝕖𝟠:𝕕𝟘:𝕗𝕔:𝕖𝟠:𝟛𝕒:𝟛𝟘"""
print(x)
print("")


m = "[+] Usage>>> python mac_changer.py -i <enter your network interface> -m <enter your new mac address you like>"
print("")
for x in m:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.02)
print ()
print("")

z = "[+] Example>>>sudo python mac_changer.py -i wlan0 -m e8:d0:fc:e8:3a:30"
for x in z:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.02)

print("")
print("")
import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC for,  use --help for usage")
    parser.add_option("-m", "--mac", dest="new_mac", help="Specify the new MAC , use --help for usage")
    (options, agruments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface, use --help for usage")
    elif not options.new_mac:
        parser.error("[-] Please specify MAC , use --help for usage")
    return options



options = get_arguments()
change_mac(options.interface, options.new_mac)
print("")
os.system("ifconfig")
