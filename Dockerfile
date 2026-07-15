FROM python:3.12-slim

WORKDIR /app

COPY Python/audit.py /app/audit.py

RUN pip install --no-cache-dir boto3

CMD ["python", "audit.py"]