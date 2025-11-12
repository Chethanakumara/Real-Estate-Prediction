# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Change working directory to where manage.py is
WORKDIR /app/RealEstatePredictor

# Collect static files (ignore errors if not configured)
RUN python manage.py collectstatic --noinput || true

# Expose Django port
EXPOSE 8000

# Run Gunicorn using the correct module path
CMD ["gunicorn", "RealEstatePredictor.wsgi:application", "--bind", "0.0.0.0:8000"]
