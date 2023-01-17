import socket
from socket import *
import time
import logging
import pyfiglet
import os

clear = lambda: os.system('cls')
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
startT = time.time()
log = logging.getLogger('SYS')

def getPortRange(ports):
    ports = ports.split(',')
    return ports[0], ports[1]


if __name__ == '__main__':
    clear()
    print(ascii_banner)
    host = input("Enter Host Address: ")
    h_IP = gethostbyname(host)
    port = input("Enter Port range (start,end):")
    p_start, p_end = getPortRange(port)
    clear()

    print(ascii_banner)

    print("-" * 50)
    print(f"\tScanning Target: {h_IP}")
    print(f"\tScanning Ports: {p_start} - {p_end}")
    print("-" * 50)


    for i in range(int(p_start), int(p_end)):
        sock = socket(AF_INET, SOCK_STREAM)

        conn = sock.connect_ex((h_IP, i))
        if(conn == 0) :
            print(f'Port {i}: OPEN')
        sock.close()