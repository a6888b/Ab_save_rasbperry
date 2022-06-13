#! /usr/local/bin/python3.10
import connect as cn 

IP = '192.168.0.11'

USER = 'pi'
PASSWORD = 'a'

client = cn.start_socket(IP)
if not client is False: 
    print('Coonexion effectuer')
    path_or_file = input("Enter the path relative for the file or ")