from random import randint
from http.server import BaseHTTPRequestHandler, HTTPServer

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
        
print("----------------------Iniciando o servidor--------------------------")
servidor = HTTPServer( ('127.0.0.1',80), MeuRequestHandler)
print("aguardando conexão...")
servidor.handle_request()