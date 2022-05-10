import socket

import testdb

s = socket.socket()
print("Socket successfully created")
port = 12346
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
db = testdb.Mysql("root", '83355806')
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    req = c.recv(1024).decode()
    income, name = db.getTeacherIncome(req)
    tosend = str(name)+"::"+str(income)
    print(f"sending {tosend}.....")
    c.send(tosend.encode())
    c.close()
