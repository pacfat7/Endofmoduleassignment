import os
import socket
import pickle

PRINT_DATA = os.getenv('PRINT_DATA', 'True') == 'True'
SAVE_DATA = os.getenv('SAVE_DATA', 'True') == 'True'

def process_received_data(conn):
    data_type = conn.recv(1024).decode('utf-8')

    if data_type == 'dict':
        received_data = conn.recv(1024)
        data = pickle.loads(received_data)
        if PRINT_DATA:
            print("Received dictionary:", data)
        if SAVE_DATA:
            with open('received_dict.txt', 'w') as f:
                f.write(str(data))

    elif data_type == 'text':
        received_text = conn.recv(1024).decode('utf-8')
        if PRINT_DATA:
            print("Received text:", received_text)
        if SAVE_DATA:
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
