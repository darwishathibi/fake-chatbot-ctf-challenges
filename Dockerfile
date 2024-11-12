# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install flask

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

