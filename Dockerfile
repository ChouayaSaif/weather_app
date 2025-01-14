# Use the slim version of Python 3.11
FROM python:3.11-slim

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

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
COPY pip_cache /app/pip_cache
RUN pip install --no-cache-dir --find-links=/app/pip_cache -r requirements.txt --default-timeout=100
# Copy the application code
COPY . .

# Expose the application port (update if necessary)
EXPOSE 8000

# Set the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
