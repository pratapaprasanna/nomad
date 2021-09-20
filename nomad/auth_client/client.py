import os
import requests

auth_host = os.environ.get("auth_host", "0.0.0.0")
auth_port = os.environ.get("auth_port", "5000")


def validate_token(token):
    url = f"http://{auth_host}:{auth_port}/fetch"
    querystring = {"token": token}
    response = requests.request("GET", url, params=querystring)
    if response:
        return True
    return False
