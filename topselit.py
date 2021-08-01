#! /usr/bin/python3

# "Jaahdytin|7"-named plug ON/OFF webpy-server at localhost:8083

import os
import math
import time
import urllib
import web
import broadlink

web.config.debug=False

d=broadlink.discover(local_ip_address="192.168.1.11")

for x in range(len(d)):
    print(d[x].name)
    if d[x].name == "Jaahdytin|7":
        plugi=d[x]

plugi.auth()

class datoja:
    urls=()

def nappi(osoite,kuvio,x,y):
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
     "<a href="+osoite+"><img src="+kuvio+"></a>"+
    '</div>\n')

def palauta_paska(refresh=False):
    s='<html>'+\
       '<head><title>TOPSELIT</title>\n'+\
       '</head>\n'+\
       '<h1> J&Auml;&Auml;HDYTIN </h1>'+\
    nappi("ON","static/ON.png",100,100)+\
    nappi("OFF","static/OFF.png",200,100)
    return(s)

datoja.urls=('/','index')
class index:
    def GET(self):
        return palauta_paska()

datoja.urls+=('/ON','ON')
class ON:
    def GET(self):
        plugi.set_power(True)
        return palauta_paska()

datoja.urls+=('/OFF','OFF')
class OFF:
    def GET(self):
        plugi.set_power(False)
        return palauta_paska()

os.environ["PORT"] = "8083"
if __name__ == "__main__":
    app = web.application(datoja.urls,globals())
    app.run()
