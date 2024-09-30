#!/bin/bash

# Step 1: Update the package list and install necessary system packages
sudo apt update
sudo apt install -y python3-pip python3-venv libpq-dev

# Step 2: Create a virtual environment
echo "Creating virtual environment for EasyLendPC..."
python3 -m venv easylendpc_env

# Step 3: Activate the virtual environment
source easylendpc_env/bin/activate

# Step 4: Install required dependencies from requirements.txt
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Step 5: Set up the database (PostgreSQL recommended for production)
echo "Setting up database with SQLAlchemy..."
# You may need to adjust this for your specific database configurations.
# For example, setting up a PostgreSQL database using environment variables.

# Step 6: Collect static files for production
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Step 7: Run database migrations
echo "Running migrations..."
python3 manage.py migrate

# Step 8: Start the Django development server (for testing purposes)
echo "Starting Django development server..."
python3 manage.py runserver

# For production use, you wiludo apt update
sudo apt install -y python3.8-pip python3.8-venv libpq-dev

# Step 2: Create a virtual environment
echo "Creating virtual environment for EasyLendPC..."
python3 -m venv easylendpc_env

# Step 3: Activate the virtual environment
source easylendpc_env/bin/activate

# Step 4: Install required dependencies from requirements.txt
echo "Installing dependencies..."
python3 -m pip3 install --upgrade pip3
python3 -m pip3 install -r requirements.txt

# Step 5: Set up the database (PostgreSQL recommended for production)
echo "Setting up database with SQLAlchemy..."
# You may need to adjust this for your specific database configurations.
# For example, setting up a PostgreSQL database using environment variables.

# Step 6: Collect static files for production
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Step 7: Run database migrations
echo "Running migrations..."
python3 manage.py migrate

# Step 8: Start the Django development server (for testing purposes)
echo "Starting Django development server..."
python3 manage.py runserver

# For production use, you will want to use Gunicorn or uWSGI.
echo "For production, use a production WSGI server like Gunicorn or uWSGI."udo apt update
sudo apt install -y python3.8-pip python3.8-venv libpq-dev

# Step 2: Create a virtual environment
echo "Creating virtual environment for EasyLendPC..."
python3 -m venv easylendpc_env

# Step 3: Activate the virtual environment
source easylendpc_env/bin/activate

# Step 4: Install required dependencies from requirements.txt
echo "Installing dependencies..."
python3 -m pip3 install --upgrade pip3
python3 -m pip3 install -r requirements.txt

# Step 5: Set up the database (PostgreSQL recommended for production)
echo "Setting up database with SQLAlchemy..."
# You may need to adjust this for your specific database configurations.
# For example, setting up a PostgreSQL database using environment variables.

# Step 6: Collect static files for production
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Step 7: Run database migrations
echo "Running migrations..."
python3 manage.py migrate

# Step 8: Start the Django development server (for testing purposes)
echo "Starting Django development server..."
python3 manage.py runserver

# For production use, you will want to use Gunicorn or uWSGI.
echo "For production, use a production WSGI server like Gunicorn or uWSGI."want to use Gunicorn or uWSGI.
echo "For production, use a production WSGI server like Gunicorn or uWSGI."
