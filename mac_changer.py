#!/usr/bin/env python3

import time
import subprocess
import argparse
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import pyfiglet
from random import choice

def animated_big_heading(text):
    console = Console()
    colors = ["bold red", "bold yellow", "bold green", "bold cyan", "bold blue", "bold magenta"]
    ascii_text = pyfiglet.figlet_format(text)
    
    for _ in range(3):  # Reduce loops for speed
        console.clear()
        styled_text = Text(ascii_text, style=choice(colors))
        console.print(Panel(styled_text, expand=False, border_style=choice(colors)))
        time.sleep(0.3)

def change_mac(interface, new_mac):
    print(f"\n[+] Changing MAC Address of {interface} to {new_mac}...\n")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    subprocess.call(["sudo", "ifconfig"])
    print("\n✅ MAC Address Successfully Changed!\n")

def main():
    parser = argparse.ArgumentParser(description="Change the MAC address of a network interface.")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to change MAC address")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address to assign")
    args = parser.parse_args()
    
    animated_big_heading("MAC CHANGER")
    change_mac(args.interface, args.mac)

if __name__ == "__main__":
    main()
