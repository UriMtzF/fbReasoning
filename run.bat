@echo off

:: Create venv if it does not exist
if exist venv (
    echo The virtual environment already exists
) else (
    echo Creating the virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Verify if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Flask is not installed, installing...
    pip install flask
) else (
    echo Flask is installed
)

:: Start flask app
echo Running the app
python main.py