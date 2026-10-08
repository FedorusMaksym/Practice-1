import requests

def run_requests():
    print("Сесія requests успішно створена:", requests.Session() is not None)