## Nomad

 Business logic for nomad comes here.

## Working Stack

- Python
- Docker
- mongo

## Web-framework to be used

- [Fast-api](https://fastapi.tiangolo.com/)

### Install
- create a virtual env
- peotry install
- 
```
(nomadenv) kingbird@kingbird-Inspiron-3542:~/work/wip/nomad$ cd nomad/
(nomadenv) kingbird@kingbird-Inspiron-3542:~/work/wip/nomad/nomad$ ls
__init__.py  __pycache__  adapters  auth_client  config.json  main.py  state_codes.csv  utils
(nomadenv) kingbird@kingbird-Inspiron-3542:~/work/wip/nomad/nomad$ uvicorn main:app --reload --host=0.0.0.0
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20535] using watchgod
INFO:     Started server process [20537]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
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

