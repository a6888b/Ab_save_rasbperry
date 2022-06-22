#! /usr/local/bin/python3.10
import client as cn
import path as pt
import constant


client = cn.start_socket(constant.HOST, constant.PORT)


def recursive_folder(conn, element: str): 
    cn.send_name_folder(element, conn)
    for file in pt.get_content_folder(element):
        if pt.is_file(file):
            cn.send_file(str(file), conn)
        elif pt.is_folder(file): 
            recursive_folder(conn, element)
            
    

while not client is False:
    print('Connexion effectuer')
    path_or_file = input(
        "Entrez le chemin d'accées relatife a votre fichier/dossier: "
    )
    if path_or_file in constant.ARRAY_WAY_QUIT:  # si le client entrez une commande pour stopper la connexion
        client.close()
        exit()

    if pt.path_exists(path_or_file):
        if pt.is_file(path_or_file):
            cn.send_file(path_or_file, client)

        elif pt.is_folder(path_or_file):
            recursive_folder(client, path_or_file)
