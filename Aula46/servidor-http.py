from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json



contato_lista = []

def cadastrar( contato):
    contato_dic = {
        "nome": contato.nome,
        "telefone": contato.telefone,
        "email": contato.email, 
}
       
    response = requests.post( url, json=contato, timeout=100 )
    return response
    
class MeuRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        
        texto_json = json.dumps(contato_lista)
        self.wfile.write( texto_json.encode('utf-8') )
        
    def do_POST(self):
        self.send_response(200)       
        self.send_header("content-type", "application/json")
        self.end_headers()
        
        lenght = int(self.headers.get('content-lenght'))
        contato = self.rfile.read()
        
        
print("----------------------Iniciando o servidor--------------------------")
servidor = HTTPServer( ('127.0.0.1',80), MeuRequestHandler)
print("aguardando conexão...")
servidor.serve_forever()