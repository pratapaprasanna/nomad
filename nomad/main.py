# App's Main page

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Place holder for home
    """
    return {"message": "Welcome to nomad"}


@app.get("/places")
async def places():
    """
    Place holder for places which gives most visited
    and least visited places given a state.
    """
    return {"message": "this is where places will go"}
