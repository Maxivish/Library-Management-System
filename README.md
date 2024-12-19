# Library Management System API

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd library_management_system

2. Set up a Python Virtual Environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

3. Install Dependencies
   ```bash
   pip install -r requirements.txt

4. Initialize the Database
   ```bash
   from database import init_db
   init_db()

5. Run the Flask Application
   ```bash
   python app.py

