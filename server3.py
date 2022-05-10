import socket

def tax(income):
    income = int(income)*12
    print(income)
    if income <= 250000:
        return income
    elif 250000 < income < 500000:
        return income*0.1
    elif 500000 < income < 1000000:
        return income*0.2
    else:
        return income*0.3

s = socket.socket()
print("Socket successfully created")
port = 12347
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    req = c.recv(1024).decode()
    taxx = str(tax(req))
    print(f"sending {taxx}...")
    c.send(taxx.encode())
    c.close()
