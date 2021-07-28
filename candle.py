#! /usr/bin/python3

import broadlink,time,math,random

d=broadlink.discover()

for x in range(len(d)):
    if d[x].name == "lamppu|9":
        lamppu=d[x]

lamppu.auth()
lamppu.set_state(pwr=1)

while True:
    b=random.randint(1,100)
    lamppu.set_state(brightness=b)
    c=random.randint(2700,6500)
    lamppu.set_state(colortemp=c)
    time.sleep(1)
