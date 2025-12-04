# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements if exists
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy project files
COPY . .

# Expose port (Django default is 8000, but your compose uses 5000)
EXPOSE 5000

# Run migrations and start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
