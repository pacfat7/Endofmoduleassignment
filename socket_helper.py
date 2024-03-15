class SocketHelper:
    @staticmethod
    def send(s, data):
        s.sendall(data)
        s.sendall(b"\n")
    
    # https://stackoverflow.com/a/74697227
    @staticmethod
    def recv(s):
        buf = []
        while True:
            c = s.recv(1)
            if not len(c):
                # socket closed
                return None
            if c == b"\n":
                return b"".join(buf)
            buf.append(c)
