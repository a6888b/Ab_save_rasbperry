import os
import socket

import constant

folder_change = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('', constant.PORT))  # ouvre le socket sur cette la machine
except OSError:
    print('Attendez que le serveur s\' eteigne completement')
    exit()

s.listen()

while True:
    conn, addr = s.accept()
    contents = conn.recv(1024).decode()
    
    if folder_change: # condition pour voir si l'arborescence a ete changer 
        os.chdir('../') # descend d'une arboresence 

    if constant.NAME_FOLDER_VARIABLE in contents:  # si c'est un nom de dossier qui est envoyez
        folder_change = True 
        folder = contents.split(constant.NAME_FOLDER_VARIABLE)[0]

        os.mkdir(folder)  # creation dossier
        os.chdir(folder)  # changement repart actuelle par le nouveau creer

    else:
        name_file = contents.split(constant.SEPARATOR)[0]  # recupere le nom du fichier
        lines = contents.split(constant.SEPARATOR)[1].split('\n')  # recupere le contenue du fichier

        with open(name_file, 'w') as f:
            for line in lines:
                f.write(line)
