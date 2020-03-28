ARG BASE_IMAGE=python:3.7-alpine

FROM ${BASE_IMAGE} as base
COPY src/requirements.txt /
RUN pip install -r /requirements.txt

FROM base as app
WORKDIR /var/task
COPY src /var/task/

ENV PYTHONPATH "/var/task:${PYTHONPATH}"

CMD ["python3", "run.py"]
