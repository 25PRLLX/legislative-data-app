# Legislative Data App

## Overview
The Legislative Data App is a Django application that allows users to access legislative data, including the number of bills each legislator supported or opposed. The app processes data from CSV files and presents it in a user-friendly interface.

## Features
- View statistics of legislators and their voting records.
- See details about bills, including titles and primary sponsors.
- Interactive tables displaying relevant data.

## Prerequisites
- Python 3.8 or higher
- Django 5.1.1
- Required libraries (listed in `requirements.txt`)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/25PRLLX/legislative-data-app.git
   cd legislative-data-app

2. **Create a virtual environment**:
    python -m venv venv

3. **Activate the virtual environment**:
   - Windows:
        - venv\Scripts\activate
   - macOS/Linux:
        - source venv/bin/activate

4. **install dependencies**:
   - pip install -r requirements.txt

5. **Run database migrations**:
   - python manage.py migrate

6. **Load initial data**:
   - Make sure the CSV data files (bills.csv, legislators.csv, vote_results.csv, and votes.csv) are located in the /data/ directory.

## Running the application

1. python manage.py runserver

2. http://127.0.0.1:8000/legislators/

## Directory Structure
legislative-data-app/
├── manage.py                 # Main script for Django commands
├── legislators/             # App directory for legislators functionality
│   ├── __init__.py           # Empty file to mark the directory as a package
│   ├── admin.py              # Admin interface configuration (optional)
│   ├── apps.py               # App configuration file (optional)
│   ├── models.py             # Models defining database structure
│   ├── views.py              # Functions handling user requests
│   ├── urls.py               # URL routing for the app
│   ├── management/           # Directory for custom management commands
│   │   ├── __init__.py       # Empty file to mark the directory as a package
│   │   └── commands/         # Subdirectory for custom management commands
│   │       ├── __init__.py   # Empty file to mark the directory as a package
│   │       └── import_data.py # Script for importing CSV data (optional)
│   ├── migrations/           # Directory containing database migrations
│   │   └── __init__.py       # Empty file to mark the directory as a package
├── templates/               # Directory for HTML templates
│   └── legislators.html      # Template for displaying legislator information
├── data/                     # Directory for CSV data files
│   ├── bills.csv              # CSV file containing bill data
│   ├── legislators.csv        # CSV file containing legislator data
│   ├── votes.csv              # CSV file mapping votes to bills
│   └── vote_results.csv       # CSV file containing vote results
└── venv/                      # Virtual environment directory (created earlier)

## Data Sources
- bills.csv: Contains information about bills (id, title, sponsor_id).

- legislators.csv: Contains information about legislators (id, name).

- vote_results.csv: Contains voting records (id, legislator_id, vote_id, vote_type).

- votes.csv: Maps vote IDs to bill IDs (id, bill_id).
