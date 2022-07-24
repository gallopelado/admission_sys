FROM python:3.10.4-alpine
ADD . /workdir

WORKDIR /workdir

RUN \
  apk update && \
  apk add --no-cache --virtual build-deps gcc g++ python3-dev musl-dev libffi-dev make && \
  apk add --no-cache postgresql-dev && \
  python3 -m pip install -r packages.txt --no-cache-dir && \
  apk del build-deps gcc g++ python3-dev musl-dev libffi-dev make

CMD ["gunicorn", "-c", "config/gunicorn_config.py", "prod:create_app_for_gunicorn()"]

