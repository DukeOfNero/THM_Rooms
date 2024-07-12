import socket

target_host = 'cctv.thm'
target_port = 5000

message = 'Hello, CCTV!'.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 5000))

sock.sendto(message, (target_host, target_port))

sock.close()
