FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir dbt-duckdb==1.10.1

# cli tool, not a server. proves the image builds
CMD ["dbt", "--version"]
