FROM python:3.12-slim

LABEL maintainer="StefVuck"
LABEL description="Generate beautiful visualizations of GitHub language usage"

WORKDIR /action

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /action/entrypoint.sh

ENTRYPOINT ["/action/entrypoint.sh"]
