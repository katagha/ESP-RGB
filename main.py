import socket
import network
from machine import Pin,PWM
#65536 100%

# Initialize PWM pins for RGB control
R =  PWM(Pin(14, Pin.OUT))
G =  PWM(Pin(12, Pin.OUT))
B =  PWM(Pin(13, Pin.OUT))

# HTTP response headers
HEADER = "HTTP/1.1 200 OK\r\n"
HEADER += "Content-Type: text/html\r\n"
HEADER += "Access-Control-Allow-Origin: *\r\n"
HEADER += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
HEADER += "Access-Control-Allow-Headers: Content-Type\r\n"
HEADER += "Connection: Keep-Alive\r\n\r\n"

def setup_ap():#Configure ESP as an access point.

    ap=network.WLAN(network.WLAN.IF_AP)
    ap.config(ssid='ESP-RGB',key="test1234")
    ip=ap.ifconfig(("10.0.0.1","255.255.255.0","10.0.0.1","10.0.0.1"))
    ap.active(True)

def set_rgb_color(Hex_Color):#Set RGB LED color based on a hex code.

    r= int(Hex_Color[:2],16)
    g= int(Hex_Color[2:4],16)
    b= int(Hex_Color[4:],16)

    print("RGB :"+str(r)+" "+str(g)+" "+str(b))
    R.duty_u16(r*65536//255)
    G.duty_u16(g*65536//255)
    B.duty_u16(b*65536//255)



def init_server():#Initialize and start the server.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.1', 8080))
    s.listen(5)
    print('[+] Server started, listening on 10.0.0.1:8080')
    return s


class WebServer:#Web server class to handle requests.

    def __init__(self,path,header,socket):
        self.path = path
        self.header = header
        self.socket = socket
    def Load(self):#Accept incoming connection.
        global conn
        conn, addr = self.socket.accept()
    def Send(self):#Send response with the requested file content.

        conn.sendall((self.header + open(self.path , "r").read()).encode("utf-8"))

    def Recv(self):#Receive data from the client.
        return conn.recv(1024).decode("utf-8")

    def Close(self):#Close the connection.
        conn.close()


def handle_request(REQ):#Process GET and POST requests.
    try:
        if "GET" in REQ :
            r=REQ.split("GET")[1].split("HTTP/")[0].split("/")[1].strip()
            f=open(f"{r}","r").read()
            conn.sendall((HEADER+f).encode("utf-8"))
        elif "POST" in REQ :
            color=REQ.split('COLOR":"')[1].split('"}')[0].lstrip("#")
            set_rgb_color(str(color))

    except :
        print("ERROR HANDLING REQ " + r )


def main ():
    setup_ap()
    server = WebServer("index.html",HEADER,init_server())
    while True :
        server.Load()
        handle_request(server.Recv())
        server.Close()

if __name__ == "__main__":
    main()
