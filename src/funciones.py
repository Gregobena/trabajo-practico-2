import string 
import random as rd 
import datetime as dt 

numeros = string.digits

# Activ 4

def mayuscula (cadena):
    tiene_mayuscula = False
    for caracter in cadena:
        if caracter.isupper():
            tiene_mayuscula = True
            break
    return tiene_mayuscula 

def un_numero (cadena):
    numeros = string.digits
    tiene_numeros = False 
    for numero in numeros: 
        if cadena.find(numero) != -1: 
            tiene_numeros = True
            break 
    return tiene_numeros 

def es_ascii (cadena): 
    ok = True 
    letras = string.ascii_letters
    for caracter in cadena:
        if (caracter in numeros) or (caracter in letras): 
            continue
        else: 
            ok = False
            break
    return ok 
            

# Activ 7 

def random_code (cadena):
    letras_numeros = string.digits + string.ascii_uppercase
    for i in range(30 - len(cadena)):
        cadena += letras_numeros[rd.randint(0,35)]
    return cadena 

# Activ 8 

def son_anagramas(cadena1,cadena2): 
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    if sorted(cadena1) == sorted(cadena2):
        return True 
    else: 
        return False 

# Activ 9

def limpiar_vacios (cadena): 
    new_clients = list() 
    for nombre in cadena:
        if nombre == None or nombre == "" or nombre == " ":
            continue 
        else:
            new_name = nombre.title().strip()
            if new_name not in new_clients: 
                new_clients.append(new_name) 
    return new_clients 

# Activ 10 

def find_points(round):
    list_points = list()
    for player in round:
        points = 0 
        for stats in round[player]:
            if stats == 'kills': 
                points += round[player][stats] * 3
            elif stats == 'assists': 
                points += round[player][stats]  
            elif stats == 'deaths' and round[player][stats] == True: 
                points -= 1
        list_points.append(points) 
    return list_points

def find_mvp(list_points):
    max = 0 
    for i in range(len(list_points)): 
        if list_points[i] > max:
            max = list_points[i]
            index = i 
    return index

def insertar_ronda(round,total):
    list_points = find_points(round)
    index_mvp = find_mvp(list_points)
    i = -1 
    for player in total:
        i += 1
        for stats in total[player]:
            if stats == 'deaths' and round[player][stats] == True:
                total[player][stats] += round[player][stats]
            elif stats == 'mvp':
                if i == index_mvp: 
                    total[player][stats] += 1
            elif stats == 'points':
                total[player][stats] += list_points[i]
            else: 
                total[player][stats] += round[player][stats]
    return total