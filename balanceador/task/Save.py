from flask import jsonify
import requests


'''
GUARDARA LA INFORMACION EN EL SERVIDOR A
@url direccion ip del servidor A
@data la informacion a almacenar
'''
def guardarServidorA(url,data):
    resultado = requests.post(url + 'guardarOracion', json = data)
    if(resultado.status_code != 200):
        #print(resultado.text)
        response = jsonify({
            'status': 400,
            'data' : 'Error al guardar en  el Servidor A'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response 
    
    response = jsonify({
        'status': 200,
        'data' : 'Guardado en el Servidor A'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 
    



'''
GUARDARA LA INFORMACION EN EL SERVIDOR B
@url direccion ip del servidor B
@data la informacion a almacenar
'''
def guardarServidorB(url,data):
    resultado = requests.post(url + 'guardarOracion', json = data)
    if(resultado.status_code != 200):
        response = jsonify({
            'status': 400,
            'data' : 'Error al guardar en  el Servidor B'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response 
    
    response = jsonify({
        'status': 200,
        'data' : 'Guardado en el Servidor B'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

#Enviara una notificacion que ambos servidores estan caidos
def errorGuardar():
    response = jsonify({
        'status': 400,
        'data' : 'Ambos servidores estan caidos'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


