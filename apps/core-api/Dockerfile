FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements /app/requirements

RUN python -m pip install --upgrade pip \
    && pip install -r /app/requirements/base.txt

COPY . /app

EXPOSE 8000

CMD ["sh", "/app/docker/entrypoint.sh"]
