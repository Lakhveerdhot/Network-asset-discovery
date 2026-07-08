from scanner.port_scanner import PortScanner

scanner = PortScanner()

ip = "192.168.31.1"

port = 80

if scanner.scan_single_port(ip, port):

    print("Port is OPEN")

else:

    print("Port is CLOSED")