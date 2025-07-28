FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set work directory
WORKDIR /app

# First install just requirements.txt to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the application
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run application
CMD ["gunicorn", "DjangoWebProject1.wsgi:application", "--bind", "0.0.0.0:8000"]