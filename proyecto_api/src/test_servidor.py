import unittest
from http.server import HTTPServer
from threading import Thread
import http.client
import json
import urllib.parse
import time
from servidor import MiManejador, PORT_API

class TestMiManejador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Iniciar el servidor en un hilo aparte
        cls.server = HTTPServer(('', PORT_API), MiManejador)
        cls.server_thread = Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        # Detener el servidor
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def test_get_request(self):
        conn = http.client.HTTPConnection('localhost', PORT_API)
        start_time = time.time()
        conn.request('GET', '/get')
        response = conn.getresponse()
        end_time = time.time()
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Solicitud GET recibida correctamente")
        print(f"GET request took {end_time - start_time:.4f} seconds")

    def test_post_request_success(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        params = urllib.parse.urlencode({'titulo': 'test'})
        conn = http.client.HTTPConnection('localhost', PORT_API)
        start_time = time.time()
        conn.request('POST', '/post', params, headers)
        response = conn.getresponse()
        end_time = time.time()
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Solicitud recibida correctamente")
        print(f"POST request (success) took {end_time - start_time:.4f} seconds")

    def test_post_request_failure(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        params = urllib.parse.urlencode({})
        conn = http.client.HTTPConnection('localhost', PORT_API)
        start_time = time.time()
        conn.request('POST', '/post', params, headers)
        response = conn.getresponse()
        end_time = time.time()
        self.assertEqual(response.status, 400)
        data = json.loads(response.read().decode())
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "El parámetro 'titulo' es requerido y no puede estar vacío.")
        print(f"POST request (failure) took {end_time - start_time:.4f} seconds")

    def test_put_request_success(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        params = urllib.parse.urlencode({'titulo': 'test'})
        conn = http.client.HTTPConnection('localhost', PORT_API)
        start_time = time.time()
        conn.request('PUT', '/put', params, headers)
        response = conn.getresponse()
        end_time = time.time()
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Solicitud recibida correctamente")
        print(f"PUT request took {end_time - start_time:.4f} seconds")

    def test_delete_request_success(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        params = urllib.parse.urlencode({'titulo': 'test'})
        conn = http.client.HTTPConnection('localhost', PORT_API)
        start_time = time.time()
        conn.request('DELETE', '/delete', params, headers)
        response = conn.getresponse()
        end_time = time.time()
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Solicitud DELETE recibida correctamente")
        print('llego')
        print(f"DELETE request took {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    unittest.main()