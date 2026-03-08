# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (since your project uses uv.lock)
RUN pip install uv

# Install Python dependencies
RUN uv pip install --system -r pyproject.toml

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run both services
CMD bash -c "uvicorn server.main:app --host 0.0.0.0 --port 8000 & streamlit run client/app.py --server.port 8501 --server.address 0.0.0.0"