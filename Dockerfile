# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 8000

# Run your app using Gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
