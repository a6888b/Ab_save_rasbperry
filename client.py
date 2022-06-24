import socket

import constant
from path import get_name


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
    name_file = get_name(file)
    with open(file) as f:
        try:
            # envoie du nom de fichier avec 6 quote pour differencier le nom du fichier est son contennue
            conn.sendall(f"{name_file}{constant.SEPARATOR}{f.read()}".encode('utf-8'))
        except BrokenPipeError:
            return False
        except ConnectionResetError:
            conn.close()
            exit('stop')


def send_name_folder(path, conn: socket.socket):
    name = get_name(path)

    try:
        conn.sendall(f'{constant.NAME_FOLDER_VARIABLE}:{name}'.encode('utf8'))
    except BrokenPipeError:
        return False
    except ConnectionResetError:
        conn.close()
        exit('stop')
