# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install unzip tool
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make the unzip script executable
RUN chmod +x data.sh

# Run the unzip script
RUN ./data.sh

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir virtualenv && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Set the virtual environment as the default Python
ENV PATH="/app/venv/bin:$PATH"

# Run pytest by default
CMD ["pytest"]
