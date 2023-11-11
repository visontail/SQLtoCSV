# Database Viewer with wxPython
## Description

The application's main feature is to save the content of tables from a MySQL Database using a wxPython GUI and export it to a CSV file.

## Installation

1. Clone the repository:

   ```
   git clone [this-repository's-url]
   ```

2. Navigate to the project directory:

   ```
   cd SQLtoCSV
   ```

3. Create a .venv
  
   ```
   # macOS / Linux
   python3 -m venv .venv
   # Windows
   python -m venv .venv
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the application in .venv:

   ```
   src/main.py
   ```

3. The application window will appear, displaying a list of tables from the connected MySQL Database.

4. Check the tables you want to save as CSV using checkboxes in the first column. You can select multiple tables as well, the application will export each in a separate file.

5. Click the "Save" button to save the selected table(s) in the `csv-files` folder.

6. CSV files will appear in the `csv-files` folder, named after their respective tables, `[table-name].CSV`.

## Folder Structure

```
├── src/
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   └── gui/
│       ├── __init__.py
│       └── app.py
│
├── venv/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

## Configuration

Create a `.env` configuration file to provide your MySQL database connection details.
The file should look like the following to match the `src/database/database.py` file which handles the database connection.

```
  HOST = 'x.x.x.x'
  USERNAME = 'username'
  PASSWORD = 'password'
  DATABASE = 'database-name'
```

## Note

- The `csv-files` folder will be automatically created if not created previously in the project directory to store the saved CSV files.
- Adjust the MySQL database connection details in `src/database/database.py` and in `.env` files as described before in order to connect properly to your database.

