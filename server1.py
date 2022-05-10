import socket
import testdb
import concurrent.futures

import connector

s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    intt = c.recv(1024).decode()
    usr, passw = intt.split("::")
    conn = testdb.Mysql("root", '83355806')
    try:
        id = str(conn.getTeacherId(usr, passw)[0])
        t = connector.tr

        #Thread calling server to fetch user name, salary
        with concurrent.futures.ThreadPoolExecutor() as executor:
            fut = executor.submit(t, id, 12346)
            name, income = fut.result().split("::")

        response1 = "Name: "+name
        response2 = "Id: "+id

            # c.send(response.encode())

        #Thread calling server3 to calaculate the income tax
        with concurrent.futures.ThreadPoolExecutor() as executor:
            fut = executor.submit(t, income, 12347)
            tax = int(float(fut.result()))

        income = int(float(income))*12
        response3 = 'Gross Pay: '+ str(income)
        response4 = "tax applied: "+ str(tax)
        response5 = "Net Pay:" + str(int(income-tax))

        response = f"\n{response1}\n{response2}\n{response3}\n{response4}\n{response5}"

        c.send(response.encode())

    except TypeError:
        c.send("wrong user".encode())

    c.close()

