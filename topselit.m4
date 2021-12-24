#! /usr/bin/python3
"""
Ikäviä m4 makroja:
undefine(`len')
undefine(`eval')
"""
import os, math, time, urllib, web, broadlink

os.chdir('/home/tnoko/Clas_Olhson/')

web.config.debug=False

d=broadlink.discover(local_ip_address="192.168.1.11")

plug1=0;plug2=0;plug3=0
while plug1==0 and plug2==0 and plug3==0:
    for x in range(len(d)):
        print(d[x].name)
        if d[x].name == "Jaahdytin|7":
            plug1=d[x]
        if d[x].name == "Tuuletin|7":
            plug2=d[x]
        if d[x].name == "pis|4":
            plug3=d[x]

def valo(d,x,y):
    try:
        if d.check_power():
            p="VALO.png"
        else:
            p="TYHJA.png"
        return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
        "<img src=static/"+p+">"+
        '</div>\n')
    except:
        return " "

def otsikko(kuvio,x,y):
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
    '<h1>'+ kuvio + '</h1>'+
    '</div>\n')

def nappi(osoite,kuvio,x,y):
    return('<div style="position: absolute; left:'+str(x)+'; top:'+str(y)+'">'+
     "<a href="+osoite+"><img src="+kuvio+"></a>"+
    '</div>\n')

define(napit,otsikko($1,100,$3-70)+\
    nappi("ON$2","static/ON.png",100,$3)+\
    valo(plug$2,180,$3)+\
    nappi("OFF$2","static/OFF.png",260,$3))

def palauta_html(refresh=False):
    s='<html><head> <title>TOPSELIT</title>\n </head>\n'+\
    napit('J&Auml;&Auml;HDYTIN/L&Auml;MMITIN',1,100)+\
    napit('TUULETIN',2,300)+\
    napit('PI',3,500)
    return(s)

define(webbinappi,
try:
    plug$1.auth()
    datoja.urls+=('/ON$1','ON$1')
    class ON$1:
        def GET(self):
            plug$1.set_power(True)
            return palauta_html()
    datoja.urls+=('/OFF$1','OFF$1')
    class OFF$1:
        def GET(self):
            plug$1.set_power(False)
            return palauta_html()
except:
    pass)

class datoja:
    urls=()

datoja.urls=('/','index')
class index:
    def GET(self):
        return palauta_html()
webbinappi(1)
webbinappi(2)
webbinappi(3)

os.environ["PORT"] = "8083"
if __name__ == "__main__":
    app = web.application(datoja.urls,globals())
    app.run()
