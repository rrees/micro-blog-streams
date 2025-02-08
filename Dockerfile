ARG PYTHON_VERSION=3.13.0

FROM python:${PYTHON_VERSION} AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIPENV_VENV_IN_PROJECT=1 \
    PIPENV_CUSTOM_VENV_NAME=.venv

WORKDIR /app
COPY . .

RUN pip install pipenv && pipenv install

FROM python:${PYTHON_VERSION}-slim-bookworm

ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y upgrade 

WORKDIR /app
COPY --from=builder /app .

RUN pip install pipenv

CMD [ "pipenv", "run", "gunicorn", "--bind=0.0.0.0:8080", "--worker-tmp-dir", "/dev/shm",   "app.app:app"]
