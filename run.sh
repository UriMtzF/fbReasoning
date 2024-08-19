#!/bin/bash

if [ -d venv ]; then
  echo "The virtual environment already exists"
else
  echo "Creating the virtual environment..."
  python3 -m venv venv
fi

source venv/bin/activate

# Verify if Flask is installed
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
  echo "Flask is not installed, installing..."
  pip3 install flask
else
  echo "Flask is installed"
fi

echo "Running the app"
python3 main.py