#! /usr/bin/python3


import os
import math
import time
import urllib
import web
import broadlink

os.chdir('/home/tnoko/Clas_Olhson/')

web.config.debug=False

d=broadlink.discover(local_ip_address="192.168.1.11")

for x in range(len(d)):
    print(d[x].name)
    if d[x].name == "Jaahdytin|7":
        plug1=d[x]
    if d[x].name == "Tuuletin|7":
        plug2=d[x]
    if d[x].name == "pis|4":
        plug3=d[x]

plug1.auth()
plug2.auth()
plug3.auth()

class datoja:
    urls=()

def check(d,x,y):
    if d.check_power():
        p="VALO.png"
    else:
        p="TYHJA.png"
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
    "<img src=static/"+p+">"+
    '</div>\n')

def otsikko(kuvio,x,y):
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
    '<h1>'+ kuvio + '</h1>'+
    '</div>\n')

def nappi(osoite,kuvio,x,y):
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
     "<a href="+osoite+"><img src="+kuvio+"></a>"+
    '</div>\n')

def palauta_paska(refresh=False):
    s='<html>'+\
       '<head><title>TOPSELIT</title>\n'+\
       '</head>\n'+\
    otsikko(' J&Auml;&Auml;HDYTIN',100,30)+\
    nappi("ON1","static/ON.png",100,100)+\
    check(plug1,180,100)+\
    nappi("OFF1","static/OFF.png",260,100)+\
    otsikko('TUULETIN',100,230)+\
    nappi("ON2","static/ON.png",100,300)+\
    check(plug2,180,300)+\
    nappi("OFF2","static/OFF.png",260,300)+\
    otsikko('PI',100,430)+\
    nappi("ON3","static/ON.png",100,500)+\
    check(plug3,180,500)+\
    nappi("OFF3","static/OFF.png",260,500)
    return(s)

datoja.urls=('/','index')
class index:
    def GET(self):
        return palauta_paska()

datoja.urls+=('/ON1','ON1')
class ON1:
    def GET(self):
        plug1.set_power(True)
        return palauta_paska()

datoja.urls+=('/OFF1','OFF1')
class OFF1:
    def GET(self):
        plug1.set_power(False)
        return palauta_paska()

datoja.urls+=('/ON2','ON2')
class ON2:
    def GET(self):
        plug2.set_power(True)
        return palauta_paska()

datoja.urls+=('/OFF2','OFF2')
class OFF2:
    def GET(self):
        plug2.set_power(False)
        return palauta_paska()

datoja.urls+=('/ON3','ON3')
class ON3:
    def GET(self):
        plug3.set_power(True)
        return palauta_paska()

datoja.urls+=('/OFF3','OFF3')
class OFF3:
    def GET(self):
        plug3.set_power(False)
        return palauta_paska()

os.environ["PORT"] = "8083"
if __name__ == "__main__":
    app = web.application(datoja.urls,globals())
    app.run()
