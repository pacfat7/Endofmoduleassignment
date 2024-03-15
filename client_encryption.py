import client_config
import socket
from data_helper import DataHelper
from encryption_helper import EncryptionHelper
from socket_helper import SocketHelper

def send_dictionary(s):
    data = {'key': 'value', 'number': 42}
    serialized_data = None

    # serialize dict to bytes
    if client_config.dictionary_pickling_format == 'binary':
        serialized_data = DataHelper.dict_to_binary_bytes(data)
        SocketHelper.send(s, b'binary_dict')
    elif client_config.dictionary_pickling_format == 'json':
        serialized_data = DataHelper.dict_to_json_bytes(data)
        SocketHelper.send(s, b'json_dict')
    elif client_config.dictionary_pickling_format == 'xml':
        serialized_data = DataHelper.dict_to_xml_bytes(data)
        SocketHelper.send(s, b'xml_dict')
    
    # send serialized bytes
    SocketHelper.send(s, serialized_data)

def send_text_file(s, file_path):
    # open text file
    with open(file_path, 'r') as file:
        text_data = file.read()

    if (client_config.encrypt_textfile):
        print("[client] encrypting...")
        encrypted_text_data = EncryptionHelper.encrypt_str(text_data)
        
        # send encrypted text
        print("[client] ready to send encrypted text: " + encrypted_text_data)
        SocketHelper.send(s, b'encrypted_text')
        SocketHelper.send(s, encrypted_text_data.encode('utf-8'))
    else:
        # send plain text
        print("[client] ready to send text: " + text_data)
        SocketHelper.send(s, b'text')
        SocketHelper.send(s, text_data.encode('utf-8'))

# connect to server
s = socket.socket()
port = client_config.server_port
s.connect((client_config.server_ip, port))

# send dict
print("[client] sending dict...")
send_dictionary(s)

# create text file
file_path = 'textfile.txt'
with open(file_path, 'w') as file:
    file.write('This is a text file.')

# disconnect from server
s.close()

# connect to server
s = socket.socket()
s.connect((client_config.server_ip, port))

# send text file
print("[client] sending text...")
send_text_file(s, file_path)

# disconnect from server
s.close()
