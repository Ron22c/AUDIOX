FROM python:3.10-slim

# Install system build tools and audio dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    git \
    curl \
    espeak-ng \
    libsndfile1 \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app app

CMD ["python", "app/main.py"]
