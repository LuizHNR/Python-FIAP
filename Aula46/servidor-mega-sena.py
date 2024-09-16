from random import randint
from http.server import BaseHTTPRequestHandler

def numeros_mega_sena():
    numeros = []
    for i in range(6):
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
            i = i + 1
    return numeros       
    
class MeuRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Cliente se conectou e pediu um GET")
        self.send_response(200)
        
