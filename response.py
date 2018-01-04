class Response:
    def __init__(self, requests_response):
        self.body = requests_response.text
        self.status = requests_response.status_code
        self.headers = requests_response.headers
        self.json = requests_response.json()
