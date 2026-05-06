FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better caching)

COPY requirements.txt .

# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy full project

COPY . .

# Run FastAPI app

CMD ["uvicorn", "TodoApp.main:app", "--host", "0.0.0.0", "--port", "8080"]
