import socket
import constant 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    s.bind(('', constant.PORT)) # ouvre le socket sur cette la machine 
except OSError: 
    print('Attendez que le serveur s\' eteigne completement')
    exit()

s.listen()

while True: 
    conn, addr = s.accept()
    contents = conn.recv(1024).decode()
    
    name_file = contents.split('||||||')[0] # recupere le nom du fichier 
    lines = contents.split('||||||')[1].split('\n') # recupere le contenue du fichier 
    
    with open(name_file, 'w') as f:
        for line in lines: 
            f.write(line)
     
    