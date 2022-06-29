#! /usr/local/bin/python3.10
import client as cn
import path as pt
import constant


client = cn.start_socket(constant.HOST, constant.PORT)

while not client is False:
    print('Connexion effectuer')
    path_or_file = input(
        "Entrez le chemin d'accées relatife a votre fichier/dossier: "
    )
    if path_or_file in constant.ARRAY_WAY_QUIT:  # si le client entrez une commande pour stopper la connexion
        client.close()
        exit()

    if pt.path_exists(path_or_file):
        for element in pt.recursive_folder(path_or_file): 
            if pt.is_file(element):
                cn.send_file(element, client)

            elif pt.is_folder(element):
                cn.send_name_folder(element, client)
