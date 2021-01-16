import socket
import argparse

BYTE_SIZE = 2048
ENCODING = "utf-8"

def start_client(ip, port):
	addr = (ip, port)

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(addr)
	client.send("echo Client connected".encode(ENCODING))
	while 1:
		print(client.recv(BYTE_SIZE).decode(ENCODING))
		path = client.recv(BYTE_SIZE).decode(ENCODING)
		#path, output = pathAndOutput.split(":")
		command = input(f"{path}> ")
		client.send(command.encode(ENCODING))
		output = client.recv(BYTE_SIZE).decode(ENCODING)
		print(output)
		client.send(command.encode(ENCODING))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--ip', type=str)
	parser.add_argument('--port', type=int)
	args = parser.parse_args()
	ip = args.ip
	port = args.port
	start_client(ip, port)