import socket


def start_socket(host: str, port: int = 2222):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except socket.gaierror:
        return False
    except ConnectionRefusedError: 
        return False 
    
    return client


def send_file(file: str, conn: socket.socket):
    with open(file, 'rb') as f:
        try: 
            conn.sendfile(f)
        except BrokenPipeError: 
            return False 
