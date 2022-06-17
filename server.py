import socket
import constant 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    s.bind((constant.HOST, constant.PORT))
except OSError: 
    print('Attendez que le serveur s\' eteigne completement')
    exit()

s.listen()

while True: 
    conn, addr = s.accept()
    msg = conn.recv(1024).decode()    
    