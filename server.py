import socket
import argparse
import os
from _thread import *

SERVER = "[SERVER]"
CONNECTION = "[CONNECTION]"
DISCONNECT = "[DISCONNECT]"
COMMAND = "[COMMAND]"
OUTPUT = "[OUTPUT]"

BYTE_SIZE = 2048
ENCODING = "utf-8"

def handle_client(conn, addr):
	try:
		while 1:
			command = conn.recv(BYTE_SIZE).decode(ENCODING)
			print(COMMAND, command)
			executeCommand = os.popen(command).read()
			print(OUTPUT, executeCommand)
			currentPath = os.path.dirname(os.path.abspath(__file__))
			reply = currentPath
			conn.send(reply.encode(ENCODING))
			conn.send(executeCommand.encode(ENCODING))
	except socket.error:
		print(DISCONNECT, "Client", addr, "has disconnected.")

def start_server(port, maxPeople):
	ip = socket.gethostbyname(socket.gethostname())
	addr = (ip, port)

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(addr)
	print(SERVER, "Server is listening on", ip, "on port", port)
	server.listen(maxPeople)

	while 1:
		conn, addr = server.accept()
		print(CONNECTION, "New Connection:", addr)

		start_new_thread(handle_client, (conn, addr))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--port', default=5000, type=int)
	parser.add_argument('--maxPeople', default=2, type=int)
	args = parser.parse_args()
	port = args.port
	max_people = args.maxPeople

	start_server(port, max_people)