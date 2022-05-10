import socket
class Conn:

    def __init__(self,ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket()

    def connectto(self, data):
        self.s.connect((self.ip,self.port))
        if data:
            data = str(data)
            self.s.send(data.encode())
        resp = self.s.recv(1024).decode()
        self.s.close()
        return resp

def tr(data='hi',port=12346):
    ip = '127.0.0.1'
    se = Conn(ip, port)
    return se.connectto(data)
