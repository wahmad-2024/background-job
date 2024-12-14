FROM python:3.11-bookworm as modrek


WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
