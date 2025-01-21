# Stage 1: Build the base image with dependencies
FROM python:3.11-slim AS base

# Set the working directory
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install or upgrade setuptools
RUN pip install --upgrade setuptools

# Copy the requirements file (for package installation)
COPY requirements.txt .

# Install Python dependencies from the requirements file
COPY pip_cache /app/pip_cache
RUN pip install --no-cache-dir --find-links=/app/pip_cache -r requirements.txt --default-timeout=600 --index-url=https://pypi.org/simple

# Stage 2: Build the final application image
FROM base AS final

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Set the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use the pre-built base image with dependencies already installed
# FROM my-weather-app-base

# # Set the working directory
# WORKDIR /app

# # Copy the application code
# COPY . .

# # Expose the application port
# EXPOSE 8000

# # Set the command to run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
