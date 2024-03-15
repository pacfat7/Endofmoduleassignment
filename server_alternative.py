import server_config
import socket
from data_helper import DataHelper
from encryption_helper import EncryptionHelper
from socket_helper import SocketHelper

# ASSUMPTION:
# first received data is data_type
# second received data is user contents
def process_received_data(conn):
    data_type = SocketHelper.recv(conn).decode('utf-8')
    print("[server] received data type: ", data_type)

    if data_type == 'binary_dict':
        print("[server] receiving binary dict...")

        received_data = SocketHelper.recv(conn)

        if (server_config.received_content_handling == 'on_screen'):
            # data = DataHelper.binary_bytes_to_dict(received_data)
            data = DataHelper.binary_bytes_to_str(received_data)
            print(data)
        elif (server_config.received_content_handling == 'file'):
            with open('received_dict.txt', 'w') as f:
                f.write(DataHelper.binary_bytes_to_str(received_data))
                f.close()
    elif data_type == 'json_dict':
        print("[server] receiving json dict...")
        
        received_data = SocketHelper.recv(conn)

        if (server_config.received_content_handling == 'on_screen'):
            # data = DataHelper.json_bytes_to_dict(received_data)
            data = DataHelper.json_bytes_to_str(received_data)
            print(data)
        elif (server_config.received_content_handling == 'file'):
            with open('received_dict.json', 'w') as f:
                f.write(DataHelper.json_bytes_to_str(received_data))
                f.close()
    elif data_type == 'xml_dict':
        print("[server] receiving xml dict...")

        received_data = SocketHelper.recv(conn)
        # print(received_data)

        if (server_config.received_content_handling == 'on_screen'):
            # data = DataHelper.xml_bytes_to_dict(received_data)
            data = DataHelper.xml_bytes_to_str(received_data)
            print(data)
        elif (server_config.received_content_handling == 'file'):
            with open('received_dict.xml', 'w') as f:
                f.write(DataHelper.xml_bytes_to_str(received_data))
                f.close()
    elif data_type == 'text':
        print("[server] receiving text...")

        received_text = SocketHelper.recv(conn).decode('utf-8')

        if (server_config.received_content_handling == 'on_screen'):
            print(received_text)
        elif (server_config.received_content_handling == 'file'):
            with open('received_text.txt', 'w') as f:
                f.write(received_text)
                f.close()
    elif data_type == 'encrypted_text':
        print("[server] receiving encrypted text...")

        received_encrypted_text = SocketHelper.recv(conn).decode('utf-8')
        received_text = EncryptionHelper.decrypt_str(received_encrypted_text)

        if (server_config.received_content_handling == 'on_screen'):
            print(received_text)
        elif (server_config.received_content_handling == 'file'):
            with open('received_text.txt', 'w') as f:
                f.write(received_text)
                f.close()

# start server
s = socket.socket()
port = server_config.server_port
s.bind(('', port))
s.listen(5)

print("[server] Server listening...")
while True:
    c, addr = s.accept()
    print(f"[server] Connection from {addr} has been established.")
    process_received_data(c)
    c.close()

# do not stop server until manually interrupt
