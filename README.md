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

## Curl request to get all the list of places given a state

```bash
curl --request GET \
  --url http://0.0.0.0:8000/destinations \
  --header 'Content-Type: application/json' \
  --data '{
 "state": "Telangana"
}'
```
