# Use Python slim variant for better compatibility and smaller size
FROM python:3.10-slim

# Set the working directory
WORKDIR /code

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install system dependencies and Python libraries
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

# Install pytest for testing
RUN pip install pytest

# Copy and install dependencies separately for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Default command to run the Flask app, or run tests if specified
CMD ["flask", "run"]
