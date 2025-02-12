#!/usr/bin/env python
import subprocess
subprocess.call(['sudo','ifconfig'])
interface=input(str("<interface: "))
new_mac=input(str("<New Mac: "))
print("[+} Changing The Mac Address of "+ interface + " to " + new_mac )
subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
subprocess.call(["sudo" ,"ifconfig"])
