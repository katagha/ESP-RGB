import socket
import network
from machine import Pin,PWM
#65536 100%


R =  PWM(Pin(14, Pin.OUT))
G =  PWM(Pin(12, Pin.OUT))
B =  PWM(Pin(13, Pin.OUT))


HEADER = "HTTP/1.1 200 OK\r\n"
HEADER += "Content-Type: text/html\r\n"
HEADER += "Access-Control-Allow-Origin: *\r\n"
HEADER += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
HEADER += "Access-Control-Allow-Headers: Content-Type\r\n"
HEADER += "Connection: Keep-Alive\r\n\r\n"

def AP():
    ap=network.WLAN(network.WLAN.IF_AP)
    ap.config(ssid='ESP-RGB',key="test1234")
    ip=ap.ifconfig(("10.0.0.1","255.255.255.0","10.0.0.1","10.0.0.1"))
    ap.active(True)

def color_change(color):

    r= int(color[:2],16)
    g= int(color[2:4],16)
    b= int(color[4:],16)

    print("RGB :"+str(r)+" "+str(g)+" "+str(b))

    R.duty_u16(int(r*65536/255))
    G.duty_u16(int(g*65536/255))
    B.duty_u16(int(b*65536/255))




def init():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.1', 8080))
    s.listen(5)
    print('[+] Server started, listening on 10.0.0.1:8080')

    return s


class WebPage:

    def __init__(self,path,header,sock):
        self.path = path
        self.header = header
        self.sock = sock

    def Showpage(page):
        print(open(page.path , "r").read())

    def Load(page):
        global conn
        conn, addr = (page.sock).accept()
    def Send(page):

        conn.sendall((page.header + open(page.path , "r").read()).encode("utf-8"))

    def Recv(page):
        return conn.recv(1024).decode("utf-8")

    def Close(page):
        conn.close()


def Get_Handler(REQ):
    try:
        if "GET" in REQ :
            r=REQ.split("GET")[1].split("HTTP/")[0].split("/")[1].strip()
            f=open(f"{r}","r").read()

            conn.sendall((HEADER+f).encode("utf-8"))
        elif "POST" in REQ :
            color=REQ.split('COLOR":"')[1].split('"}')[0].split("#")[1]
            color_change(str(color))

    except :
        print("ERROR HANDLING THE GET REQ " + r )


def main ():
    AP()
    w = WebPage("index.html",HEADER,init())
    while True :
        w.Load()
        Get_Handler(w.Recv())
        w.Close()
main()




