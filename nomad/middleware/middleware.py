from nomad.utils import utils
from fastapi import HTTPException

from nomad.auth_client import client

from oslo_log import log as logging

LOG = logging.getLogger(__name__)


def valid_request(request):
    try:
        token = request.headers["authorization"].split(" ")[1]
        if token and token != "undefined":
            if client.validate_token(token):
                LOG.info("Token Valid")
                return True
            else:
                LOG.info("Token invalid")
                return False
        else:
            LOG.info("Token Empty hence Bad Request")
            raise HTTPException(status_code=400, detail="Bad Request")

    except KeyError:
        LOG.info("No Token hence Bad Request")
        raise HTTPException(status_code=400, detail="Bad Request")
