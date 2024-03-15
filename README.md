# Simple Client/Server Network

The project is to build a simple client/server network. Once the network is established:

1. Create a dictionary, populate it, serialize it and send it to a server.
2. Create a text file and send it to a server.

With the dictionary, the user should be able to set the pickling format to one of the following: binary, JSON and XML. Also, the user will need to have the option to encrypt the text in a text file.

The server should have a configurable option to print the contents of the sent items to the screen and or to a file. Also, the server will need to be able to handle encrypted contents.

The client and server can be on separate machines or on the same machine.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
the required modules.

```bash
pip install -r requirements.txt
```

## Usage

To run the server:

```
python server.py
```

To run the client:
```
python client.py
```

You can modify server_config.py (server configurations) and 
client_config.py (client configurations).

The server does not stop until manually interrupt.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and acknowledgment
Guru Mukadam, Hiu Kwan Rebecca Lee, Ka Kit Chua, Mausam Mistri, Rebecca Record. 
Especially thanks to the help from Mr. Stanley Mak from Hong Kong and the aid of https://www.makeareadme.com/
