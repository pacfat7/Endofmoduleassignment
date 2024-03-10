import socket
import pickle

def process_received_data(conn):
    data_type = conn.recv(1024).decode('utf-8')
    if data_type == 'dict':
        received_data = conn.recv(1024)
        data = pickle.loads(received_data)
        print("Received dictionary:", data)
    elif data_type == 'text':
        received_text = conn.recv(1024).decode('utf-8')
        print("Received text:", received_text)
        with open('received_text.txt', 'w') as f:
            f.write(received_text)

s = socket.socket()
port = 44556
s.bind(('', port))
s.listen(5)

print("Server listening...")
while True:
    c, addr = s.accept()
    print(f"Connection from {addr} has been established.")
    process_received_data(c)
    c.close()

