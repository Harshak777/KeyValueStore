FROM python:3.9

WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install python requirements
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the files
COPY . /app/

# Expose the port
EXPOSE 8000

# Run the server
CMD ["/bin/sh", "uvicorn main:app --host 0.0.0.0 --port 8000 & python3 huey_consumer.py redis_huey.huey"]
