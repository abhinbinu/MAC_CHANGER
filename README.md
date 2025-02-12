# MAC CHANGER - A Colorful MAC Address Spoofing Tool 🚀

This Python tool allows you to **change the MAC address** of a network interface with a stylish and colorful animation. It is useful for **privacy, security testing, and penetration testing**.

---

## 🎨 Features
✅ **Big, Colorful Animated Heading** using `rich` and `pyfiglet`  
✅ **Interactive User Input** for selecting a network interface and new MAC  
✅ **Automated MAC Address Change** using `ifconfig` or `ip` commands  
✅ **Works on Linux** (Tested on Kali Linux)  

---

## 🛠 Installation & Setup

### 1️⃣ Install Python (If Not Installed)
Ensure you have **Python 3** installed:
```sh
python3 --version
```
If not installed, use:
```sh
sudo apt install python3
```

### 2️⃣ Clone This Repository
```sh
git clone https://github.com/abhinbinu/MAC_CHANGER.git
cd MAC_CHANGER
```

### 3️⃣ Install Dependencies
Install the required Python libraries using `requirements.txt`:
```sh
pip install -r requirements.txt
```
(If using **Python 3**, run `pip3 install -r requirements.txt`)

---

## 🚀 Usage
Run the script with **sudo** to modify network settings:
```sh
sudo python3 mac_changer.py
```
Then, follow the prompts to enter your **network interface** (e.g., `wlan0` or `eth0`) and a **new MAC address**.

---

## 🔧 Example Run
```sh
[+] Enter Interface (e.g., eth0, wlan0): wlan0
[+] Enter New MAC Address (e.g., 00:11:22:33:44:55): 00:AA:BB:CC:DD:EE
[+] Changing MAC Address of wlan0 to 00:AA:BB:CC:DD:EE...
✅ MAC Address Successfully Changed!
```

---

## 📌 Notes
- **If `ifconfig` is deprecated**, modify the script to use `ip link` instead.
- **Only works on Linux-based systems** (Does not support Windows/MacOS).
- **You need root privileges (`sudo`)** to modify MAC addresses.

---

## 🛠 Troubleshooting
If you get a **command not found** error for `ifconfig`, install `net-tools`:
```sh
sudo apt install net-tools
```
For `ip` command issues, try:
```sh
sudo apt install iproute2
```

---

## 📜 License
This project is open-source under the **MIT License**.

---

### 🔗 Follow & Contribute
Feel free to **fork, modify, and contribute** to improve this tool! 🚀

