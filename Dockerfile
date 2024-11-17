# Dockerfile
FROM python:3.11.9-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY models/logistic_regression_model.pkl /app/
COPY src/main.py /app/

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn pydantic pandas numpy joblib

# Expose port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]