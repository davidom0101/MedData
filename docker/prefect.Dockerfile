FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir prefect==3.7.8

# no flow logic yet, just proves the server boots
CMD ["prefect", "server", "start", "--host", "0.0.0.0"]
