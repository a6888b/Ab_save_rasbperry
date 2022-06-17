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
    if pt.path_exists(path_or_file):
        if pt.is_file(path_or_file):
            cn.send_file(path_or_file, client)

        elif pt.is_folder(path_or_file):
            for file in pt.get_content_folder(path_or_file):
                if pt.is_file(file):
                    cn.send_file(str(file), client)
