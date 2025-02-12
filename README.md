# **MAC Changer**

A Python-based tool to change the MAC address of a network interface using **Rich** for a stylish CLI and **argparse** for command-line arguments.

## **Features**
✔ Animated banner using `pyfiglet` and `rich`
✔ Command-line interface with `argparse`
✔ Automates MAC address change with `ifconfig`
✔ Requires **sudo** permissions

## **Installation**
Ensure Python 3 is installed. Then, install dependencies:
```sh
pip install -r requirements.txt
```

## **Usage**
Run the script with:
```sh
sudo python3 mac_changer.py -i <interface> -m <new_mac>
```
Example:
```sh
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## **Requirements**
- Python 3  
- `rich` (for colorful output)  
- `pyfiglet` (for ASCII text)  
- `argparse` (built-in, used for CLI arguments)  

Install missing dependencies with:
```sh
pip install rich pyfiglet
```

