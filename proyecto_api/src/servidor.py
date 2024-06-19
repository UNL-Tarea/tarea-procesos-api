# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:38:14 2024

@author: Toshiba
"""
import http.server
import socketserver
import urllib.parse
import json

PORT_API = 10000
PORT_CLIENTE = '*'  # Permitir cualquier origen (para desarrollo, ajustar en producción)

class MiManejador(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/get':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', PORT_CLIENTE)
            self.end_headers()
            response = {"success": True, "message": "Solicitud GET recibida correctamente"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Página no encontrada")

    def do_POST(self):
        if self.path == '/post':
            self._handle_post_put_request()
        else:
            self.send_error(404, "Página no encontrada")

    def do_PUT(self):
        if self.path == '/put':
            self._handle_post_put_request()
        else:
            self.send_error(404, "Página no encontrada")

    def do_DELETE(self):
        if self.path == '/delete':
            self._handle_delete_request()
        else:
            self.send_error(404, "Página no encontrada")

    def _handle_post_put_request(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_put_data = self.rfile.read(content_length)
            params = urllib.parse.parse_qs(post_put_data.decode('utf-8'))
            
            if 'titulo' not in params or not params['titulo']:
                raise ValueError("El parámetro 'titulo' es requerido y no puede estar vacío.")
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', PORT_CLIENTE)
            self.end_headers()
            
            response = {"success": True, "message": "Solicitud recibida correctamente", "data": []}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', PORT_CLIENTE)
            self.end_headers()
            error_message = {"success": False, "message": str(e)}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

    def _handle_delete_request(self):
        try:
            content_length = int(self.headers['Content-Length'])
            delete_data = self.rfile.read(content_length)
            params = urllib.parse.parse_qs(delete_data.decode('utf-8'))
            
            if 'titulo' not in params or not params['titulo']:
                raise ValueError("El parámetro 'titulo' es requerido y no puede estar vacío.")
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', PORT_CLIENTE)
            self.end_headers()
            
            response = {"success": True, "message": "Solicitud DELETE recibida correctamente", "data": []}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', PORT_CLIENTE)
            self.end_headers()
            error_message = {"success": False, "message": str(e)}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

with socketserver.TCPServer(("", PORT_API), MiManejador) as httpd:
    print("SERVIDOR-PUERTO:", PORT_API)
    httpd.serve_forever()
