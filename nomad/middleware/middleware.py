from nomad.utils import utils
from fastapi import HTTPException

from nomad.auth_client import client


def valid_request(request):
    try:
        token = request.headers["authorization"].split(" ")[1]
        if token and token != "undefined":
            if client.validate_token(token):
                return True
            else:
                return False
        else:
            raise HTTPException(status_code=400, detail="Bad Request")

    except KeyError:
        raise HTTPException(status_code=400, detail="Bad Request")
