# Dependencies
- Depends on [authenticator](https://github.com/pratapaprasanna/authenticator)

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
- Create a virtual environment

 - ```pip install poetry```
 - ```poetry install```
 - ```uvicorn nomad.main:app --reload --host=0.0.0.0```

### Working APIs

## Curl request to add new places to the db

```bash
curl --request POST \
  --url http://0.0.0.0:8000/place \
  --header 'Content-Type: application/json' \
  --data '{
 "name": "Indira Park",
 "city": "hyderabad",
 "pincode": "500044",
 "state": "telangana",
 "rating": 4.0
}'
```

## Sample Response

<img width="1018" alt="Screenshot 2021-09-08 at 12 17 22 AM" src="https://user-images.githubusercontent.com/15846947/132395614-1f331e46-2ed1-405a-886a-98c64a8cf6ef.png">

## Curl request to get all the list of places given a state

```bash
curl --request GET \
  --url http://0.0.0.0:8000/destinations \
  --header 'Content-Type: application/json' \
  --data '{
 "state": "Telangana"
}'
```

## Sample Response
<img width="1034" alt="Screenshot 2021-09-08 at 12 16 51 AM" src="https://user-images.githubusercontent.com/15846947/132395563-50d84bfc-1e85-4062-adc8-4f8d31fbbab3.png">

## Documentation
[here](https://pratapaprasanna.github.io/nomad/)
