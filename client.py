import socket
import pickle

def send_dictionary(s):
    data = {'key': 'value', 'number': 42}
    serialized_data = pickle.dumps(data)
    s.sendall(b'dict')  
    s.sendall(serialized_data)

def send_text_file(s, file_path):
    with open(file_path, 'r') as file:
        text_data = file.read()
    s.sendall(b'text')  
    s.sendall(text_data.encode('utf-8'))

s = socket.socket()
port = 44556
s.connect(('127.0.0.1', port))

send_dictionary(s)

file_path = 'sample_text.txt'
with open(file_path, 'w') as file:
    file.write('This is a sample text file.')

s.close()
s = socket.socket()
s.connect(('127.0.0.1', port))

send_text_file(s, file_path)

s.close()

