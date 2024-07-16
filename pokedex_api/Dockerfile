# Pull the official base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Set environment variables to not generate pyc files and to force stdout and stderr streams to be unbuffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the system and install dependencies for the project
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    dos2unix \
    mariadb-client \
    libmariadb-dev

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Copy the Django project files into the container
COPY . .

# Copy entrypoint script into the container, convert line endings, and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Collect static files
RUN python manage.py collectstatic --noinput

# Test if Django is installed correctly
RUN python -m django --version

# Define the entrypoint script to be executed
ENTRYPOINT ["bash", "/usr/local/bin/entrypoint.sh"]
