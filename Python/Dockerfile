FROM python:3.12-slim

WORKDIR /app

COPY Python/requirements.txt ./Python/requirements.txt

RUN pip install --no-cache-dir -r Python/requirements.txt

COPY Python/audit.py ./Python/audit.py

RUN mkdir -p /app/Reports

WORKDIR /app/Python

CMD ["python", "audit.py"]