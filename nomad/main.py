# App's Main page

import os
from fastapi import FastAPI, Request

from nomad.adapters.models.request_models import Place, Destinations
from nomad.adapters.db import api as db_api
from nomad.utils import utils

host = os.environ.get("db_host", "mongo")
port = os.environ.get("db_port", "27017")

app = FastAPI()
db_obj = db_api.MongoAdapters(host, port)


@app.get("/")
async def root():
    """
    Place holder for home
    """
    return {"message": "Welcome to nomad"}


@app.get("/destinations")
async def destinations(destination: Destinations):
    """
    API to get all the destinations present in db and
    sorted as per ratings
    """
    state = utils.tailor_strings(destination.state)
    response = db_obj.get_all_destinations(state)
    return {"message": response}


@app.post("/place", status_code=201)
async def destination(place: Place):
    """
    API call to add places into db.
    """
    name = utils.tailor_strings(place.name)
    city = utils.tailor_strings(place.city)
    pincode = utils.tailor_strings(place.pincode)
    state = utils.tailor_strings(place.state)
    rating = place.rating
    tin, state_code = utils.get_state_information(state)
    response = db_obj.add_destinations(
        name, city, pincode, state, tin, state_code, rating
    )
    return response
