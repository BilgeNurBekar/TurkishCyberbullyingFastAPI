# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the entire project to the container
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command to run the FastAPI app with uvicorn
CMD ["python", "app/main.py"]
