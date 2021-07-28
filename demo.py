#! /usr/bin/python3

import broadlink,time

d=broadlink.discover(local_ip_address="192.168.1.11")
print(d)

for x in range(len(d)):
    print(d[x].name)
    if d[x].name == "Vanha|-1":
        plugi=d[x]
    if d[x].name == "pis|4":
        pi=d[x]
    if d[x].name == "lamppu|9":
        lamppu=d[x]
lamppu.auth()
lamppu.set_state(pwr=1)
print(lamppu.get_state())
lamppu.set_state(brightness=1000)
time.sleep(5)
lamppu.set_state(brightness=0)
time.sleep(5)
lamppu.set_state(pwr=0)


plugi.auth()
plugi.set_power(True)
time.sleep(5)
plugi.set_power(False)

