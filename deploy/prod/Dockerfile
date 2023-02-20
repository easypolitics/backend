FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r ./requirements/prod.txt

RUN addgroup --system easypolitics && \
    adduser --system --ingroup easypolitics easypolitics

RUN mkdir /app/static

RUN chown -R easypolitics:easypolitics /app

ENV PATH="/py/bin:$PATH"

USER easypolitics

ENTRYPOINT ["sh", "/app/deploy/prod/entrypoint.sh"]
