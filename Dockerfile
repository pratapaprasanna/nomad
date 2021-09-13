FROM python:3.8-buster as dev

RUN pip install poetry==1.0.0
ENV PATH="/root/.poetry/bin:${PATH}"

WORKDIR /app/

ADD . /app
RUN poetry install
CMD poetry run uvicorn nomad.main:app --reload --host=0.0.0.0
