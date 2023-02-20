FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    curl

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.2.1/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=d7f4c0886eb85249ad05ed592902fa6865bb9d70

RUN curl -fsSLO "$SUPERCRONIC_URL" \
    && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
    && chmod +x "$SUPERCRONIC" \
    && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
    && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

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
