# Stage 1: build
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt \
    && find /install -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true \
    && find /install -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true \
    && find /install -name "*.pyc" -delete \
    && find /install -name "*.pyo" -delete

# Stage 2: final
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /install /usr/local
COPY model_files/ ./model_files/
COPY app/ ./app/
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
