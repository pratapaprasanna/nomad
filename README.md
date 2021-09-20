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
  --url http://192.168.0.180:8000/place \
  --header 'Authorization: Bearer b53dd7a1' \
  --header 'Basic: ' \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "imax",
	"city": "hyderabad",
	"pincode": "500044",
	"state": "telangana",
	"rating": 3.75
}'
```

## Sample Response

<img width="1018" alt="Screenshot 2021-09-08 at 12 17 22 AM" src="https://user-images.githubusercontent.com/15846947/132395614-1f331e46-2ed1-405a-886a-98c64a8cf6ef.png">

## Curl request to get all the list of places given a state

```bash
curl --request GET \
  --url http://192.168.0.180:8000/destinations \
  --header 'Authorization: Bearer b53dd7a1' \
  --header 'Content-Type: application/json' \
  --data '{
	"state": "Telangana"
}'
```

## Sample Response
<img width="1034" alt="Screenshot 2021-09-08 at 12 16 51 AM" src="https://user-images.githubusercontent.com/15846947/132395563-50d84bfc-1e85-4062-adc8-4f8d31fbbab3.png">

## Wrong auth-key

```bash
curl --request GET \
  --url http://192.168.0.180:8000/destinations \
  --header 'Authorization: Bearer b53dd7a' \
  --header 'Content-Type: application/json' \
  --data '{
	"state": "Telangana"
}'
```
### Response
<img width="1027" alt="Screenshot 2021-09-20 at 1 17 06 PM" src="https://user-images.githubusercontent.com/15846947/133970582-fb3d7184-bb37-491b-8566-58448f703614.png">

## Missin auth-key
```bash
curl --request GET \
  --url http://192.168.0.180:8000/destinations \
  --header 'Authorization: Bearer ' \
  --header 'Content-Type: application/json' \
  --data '{
	"state": "Telangana"
}'
```
### Response
<img width="1028" alt="Screenshot 2021-09-20 at 1 19 56 PM" src="https://user-images.githubusercontent.com/15846947/133970870-33d0d717-150d-4be1-b818-847970b3614a.png">

## Documentation
[here](https://pratapaprasanna.github.io/nomad/)
