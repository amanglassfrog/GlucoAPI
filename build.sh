#!/bin/bash

  # Change to the directory containing manage.py

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Start the development server
python3 manage.py runserver
