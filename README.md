## Nomad

 Business logic for nomad comes here.

## Working Stack

- Python
- Docker
- mongo

## Web-framework to be used

- [Fast-api](https://fastapi.tiangolo.com/)

### Local Setup

##### Run

 - ```pip install poetry```
 - ```poetry install```
 - ```uvicorn nomad.main:app --reload --host=0.0.0.0```

### Working APIs

## Curl request to add new places to the db

```bash
curl --request POST \
  --url http://192.168.0.180:8000/place \
  --header 'Content-Type: application/json' \
  --data '{
 "name": "Indira Park",
 "city": "hyderabad",
 "pincode": "500044",
 "state": "telangana",
 "rating": 4.0
}'
```

## Curl request to get all the list of places given a state

```bash
curl --request GET \
  --url http://192.168.0.180:8000/destinations \
  --header 'Content-Type: application/json' \
  --data '{
 "state": "Telangana"
}'
```
