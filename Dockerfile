ARG PYTHON_VERSION=3.12.4
ARG HOST=0.0.0.0

FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD uvicorn app.main:app --host=${HOST}
