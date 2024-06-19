from pip import HttpUser, task, between

class test_stres(HttpUser):
    # El tiempo de espera entre las tareas se seleccionará aleatoriamente de un rango de 5 a 15 segundos
    wait_time = between(5, 15)

    @task
    def load_homepage(self):
        # Esta tarea carga la página de inicio de Google
        self.client.get("http://localhost:10000")

    @task
    def perform_search(self):
        # Esta tarea realiza una búsqueda en Google
        self.client.get("http://www.google.com/search?q=python+programming")