from socket import *
import time
import logging

startT = time.time()
log = logging.getLogger('SYS')

def getPortRange(ports):
    ports = ports.split(',')
    return ports[0], ports[1]


if __name__ == '__main__':
    host = input("Enter Host Address: ")
    h_ip = gethostbyname(h_ip)
    port = input("Enter Port range (start,end) : ")
    p_start, p_end = getPortRange(port)

    log(f'Scan Host: {h_IP}')
    log(f'Scan Ports: {p_start} - {p_end}')


    for i in range(p_start, p_end):
        socket = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            log(f'Port {i}: OPEN')
        socket.close()