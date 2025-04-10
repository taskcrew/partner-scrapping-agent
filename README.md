# Partner Scrapping Agent

A simple CrewAI-powered tool for extracting business information from websites using Firecrawl.

## Overview

This tool uses CrewAI framework to create an agent-based system that extracts business information from websites. It leverages the Firecrawl API to perform the extraction and presents the data in a structured format.

## Features

- Extract business information including:
  - Business name
  - Opening hours
  - Phone number
  - Email address
  - Wi-Fi availability
- Interactive user input for target websites
- Single-file implementation following CrewAI best practices

## Setup

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv crewai_venv
source crewai_venv/bin/activate  # On Windows: crewai_venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install crewai firecrawl python-dotenv
```

4. Create a `.env` file in the project root with your Firecrawl API key:
```
FIRECRAWL_API_KEY=your-firecrawl-api-key
```

## Usage

Run the script:
```bash
python partner-scrapping-agent.py
```

When prompted, enter the website URL you want to extract information from. Press Enter to use the default example website.

## Files

- `partner-scrapping-agent.py` - Main script containing the complete implementation
- `.env` - Environment variables file (you need to create this)

## Note

This project follows a single-file implementation approach as per the CrewAI guidelines. All components including agent definitions, task creation, and tool registration are contained within a single Python file for simplicity and self-containment.
