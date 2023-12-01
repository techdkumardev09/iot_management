# Use the official Python image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the working directory
COPY . /app/

# Run Django migrations during image build
RUN python manage.py makemigrations
RUN python manage.py migrate


# Run Django migrations during image build
RUN python manage.py makemigrations app
RUN python manage.py migrate app

