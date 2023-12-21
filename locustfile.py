from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task(2)
    def load_flask(self):
        self.client.get("http://flask-app:8000", name="flask")

    @task(2)
    def load_express(self):
        self.client.get("http://express-app:3000", name="express")
