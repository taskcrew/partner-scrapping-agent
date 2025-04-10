#!/bin/bash
# Setup script for CrewAI v0.108.0 with Python 3.10-3.12 using uv

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing uv..."
    # Install uv using the recommended method
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Check if Python 3.10-3.12 is available
if command -v python3.10 &> /dev/null; then
    PYTHON_CMD="python3.10"
elif command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
elif command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
else
    echo "Error: Python 3.10, 3.11, or 3.12 is required but not found."
    echo "Please install Python 3.10-3.12 before continuing."
    exit 1
fi

echo "Using $PYTHON_CMD for the environment"

# Create a virtual environment using uv
echo "Creating virtual environment..."
uv venv -p $PYTHON_CMD crewai_venv

# Activate the virtual environment
echo "Activating virtual environment..."
source crewai_venv/bin/activate

# Install packages using uv
echo "Installing packages with uv..."
uv pip install crewai==0.108.0 firecrawl-py python-dotenv

# Copy environment file
echo "Setting up environment file..."
cp .env.v108 crewai_venv/.env

# Copy the business_data_crew.py file to a new file for the v0.108.0 implementation
cp business_data_crew.py business_data_crew_v108.py

echo "Setup complete! To activate the environment and run the example:"
echo ""
echo "source crewai_venv/bin/activate"
echo "cd crewai_venv"
echo "python ../business_data_crew_v108.py" 