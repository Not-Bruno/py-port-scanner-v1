import socket
import time
import pyfiglet
import os
from colorama import init, Fore

# Colorization
init()
SUCC = Fore.GREEN
ERR = Fore.RED
WARN = Fore.YELLOW
RESET = Fore.RESET


clear = lambda: os.system('cls') # Clear Terminal
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") # create ASCII Banner
timeX = time.time() # set Timestamp

def getPortRange(ports):
    ports = ports.split(',')
    return ports[0], ports[1]


if __name__ == '__main__':
    clear()
    print(ascii_banner)
    host = input("Enter Host Address: ")
    h_IP = socket.gethostbyname(host)
    port = input("Enter Port range (start,end):")
    p_start, p_end = getPortRange(port)
    clear()

    print(ascii_banner)

    print("-" * 50)
    print(f"\tScanning Target: {h_IP}")
    print(f"\tScanning Ports: {p_start} - {p_end}")
    print("-" * 50)


    for i in range(int(p_start), int(p_end)):
        sock = socket.socket()

        try:
            conn = sock.connect((h_IP, i))
            if(conn == 0) :
                print(f'Port {i}: {SUCC}OPEN{RESET}')
            sock.close()
        except Exception as e:
            print(f'Port {i}: {ERR}CLOSE{RESET}')
            pass