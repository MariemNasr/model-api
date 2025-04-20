# Use an official Python runtime
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
