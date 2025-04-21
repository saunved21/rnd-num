# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to be accessed outside the container
EXPOSE 8080

# Define the default command to run the application
CMD ["python", "code.py"]
