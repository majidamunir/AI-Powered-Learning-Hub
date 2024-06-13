# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file first for better caching of dependencies
COPY requirements.txt /code/

# Create and activate a virtual environment, then install dependencies
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY ./Elearning /code/

# Create SQLite3 database file
RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
