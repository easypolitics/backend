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
    /py/bin/pip install -r ./requirements/dev.txt

RUN addgroup --system easypolitics && \
    adduser --system --ingroup easypolitics easypolitics

RUN chown -R easypolitics:easypolitics /app

ENV PATH="/py/bin:$PATH"

USER easypolitics

ENTRYPOINT ["sh", "./deploy/dev/entrypoint.sh"]
