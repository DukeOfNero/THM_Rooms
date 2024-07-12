import requests
import socket


message = 'Hello, CCTV!'.encode()

target_host = 'cctv.thm'
target_port = 443


def send_tcp_request(dtarget_host, dtarget_port, dmesg):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		sock.connect((dtarget_host, dtarget_port))
	
		sock.sendall(dmesg.encode())
	
		data = sock.recv(1024)
	
		print(data.decode())	

	finally:
		sock.close()


url = 'https://cctv.thm/fpassword.php?id=2'

send_tcp_request(target_host, target_port, "GET /fpassword.php?id=2\r\nHost:cctv.thm\r\nUser-Agent: I am Steve Friend\r\n\r\n")
