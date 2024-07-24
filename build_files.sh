#!/usr/bin/env bash
# exit on error
set -o errexit

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Build CSS with Tailwind
echo "Building CSS..."
npm run build-css

echo "Make Migration..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear