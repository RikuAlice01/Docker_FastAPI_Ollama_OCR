FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN apt-get update && apt-get install -y curl

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8000

ENTRYPOINT ["/app/start.sh"]
