# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Upgrading pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the source code into the container
COPY . .

# Inject variables from railway
ARG POSTGRES

# Set environment variables
ENV POSTGRES=$POSTGRES

# Expose the port the gRPC service runs on
EXPOSE 4040

# Command to run the application
CMD ["python", "main.py"]
