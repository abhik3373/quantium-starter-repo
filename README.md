📊 Quantium Software Engineering Virtual Experience

This repository contains my completed work for the Quantium Software Engineering Virtual Experience Program hosted on Forage.
The project simulates real-world software engineering tasks including data processing, dashboard development, testing, and test automation using Python and Dash.

🧠 Project Overview

Soul Foods, a fictional client, experienced a decline in sales for their top-performing product — Pink Morsels.
The objective of this project was to:

Process raw transaction data

Build an interactive data visualisation

Enable region-based analysis

Validate the application using automated tests

Prepare the project for Continuous Integration (CI)

The final outcome is an interactive Dash application that clearly answers:

“Were sales higher before or after the Pink Morsel price increase on 15 January 2021?”

🛠️ Technologies Used

Python 3

Dash (Data Visualisation)

Pandas (Data Processing)

Plotly (Charts)

Pytest (Testing)

Bash (Test Automation)

Git & GitHub

📁 Project Structure
quantium-starter-repo/
│
├── app.py                     # Dash application
├── data/
│   ├── raw_sales_data_0.csv   # Original datasets
│   └── processed_sales_data.csv
│
├── tests/
│   └── test_app.py            # Automated tests
│
├── run_tests.sh               # CI-style test automation script
├── venv/                      # Virtual environment
└── README.md

🔍 Tasks Completed
✅ Task 1: Environment Setup

Forked and cloned starter repository

Configured Python virtual environment

Installed required dependencies

✅ Task 2: Data Processing

Combined multiple CSV files

Filtered data for Pink Morsels

Created calculated sales field

Exported clean, analysis-ready dataset

✅ Task 3: Dash Application

Built interactive line chart

Visualised sales trends over time

Clearly highlighted price change impact

✅ Task 4: UI Enhancements

Added region-based radio filter

Improved layout and styling using CSS

Enhanced usability and clarity

✅ Task 5: Automated Testing

Implemented pytest test suite

Verified:

Header presence

Graph presence

Region filter presence

⭐ Task 6 (Bonus): Test Automation

Created bash script to:

Activate virtual environment

Execute test suite

Return CI-compatible exit codes

▶️ How to Run the Application

Activate the virtual environment:

venv\Scripts\activate


Start the Dash app:

python app.py


Open your browser and visit:

http://127.0.0.1:8050

🧪 Run Tests
pytest


Or using the automated script (CI-style):

bash run_tests.sh

📈 Key Insights

Sales trends before and after 15 Jan 2021 are clearly visible

Region-wise filtering enables deeper business analysis

Automated testing ensures application reliability

🎓 What I Learned

Real-world data processing techniques

Building production-ready Dash applications

Writing UI-focused automated tests

Understanding Continuous Integration fundamentals

Debugging cross-platform testing issues (Windows + Dash)

🔗 Program Reference

Quantium Software Engineering Virtual Experience

Hosted on Forage

👤 Author

Abhishek Kolpe
Computer Science Engineer | Aspiring Software Engineer

🔗 GitHub: https://github.com/abhik3373
