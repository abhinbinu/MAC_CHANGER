#!/usr/bin/env python3

import time
import subprocess
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import pyfiglet
from random import choice

console = Console()

def animated_big_heading(text):
    colors = ["bold red", "bold yellow", "bold green", "bold cyan", "bold blue", "bold magenta"]
    
    ascii_text = pyfiglet.figlet_format(text)

    for _ in range(3):  
        console.clear()
        styled_text = Text(ascii_text, style=choice(colors))
        console.print(Panel(styled_text, expand=False, border_style=choice(colors)))
        time.sleep(0.3)


animated_big_heading("MAC CHANGER")


subprocess.call(['sudo', 'ifconfig'])


interface = input("\n[+] Enter Interface (e.g., eth0, wlan0): ").strip()
new_mac = input("[+] Enter New MAC Address (e.g., 00:11:22:33:44:55): ").strip()


print(f"\n[+] Changing MAC Address of {interface} to {new_mac}...\n")


subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])


subprocess.call(["sudo", "ifconfig"])

print("\n✅ MAC Address Successfully Changed!\n")
