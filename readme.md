
# CSV File Uploader and Data Viewer

This project is a web application that allows users to upload CSV files, store the data in a SQLite database, and view the data in a tabular format.

## Features

- Upload CSV files: Users can select and upload CSV files using the provided file input.
- Store data: The uploaded CSV data is stored in a SQLite database.
- View data: Users can retrieve and view the uploaded data in a tabular format.

## Technologies Used

- Frontend: React.js
- Backend: Python (FastAPI)
- Database: SQLite
- Additional libraries: Axios (for making HTTP requests), csv (for parsing CSV data)

## Getting Started

### Prerequisites

- Node.js and npm (Node Package Manager)
- Python 3
- SQLite

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

3. Install frontend dependencies:

```bash
npm install
```

4. Install backend dependencies (recommended to use a virtual environment):

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows
pip install -r requirements.txt
```

### Usage

1. Start the backend server:

```bash
uvicorn main:app --reload
```

2. Start the frontend development server:

```bash
npm start
```

3. Access the application in your browser at `http://localhost:3000`.

4. Upload a CSV file using the provided file input.

5. Click the "Upload Data" button to send the file to the backend, store the data in the database, and receive a success message.

6. Click the "Get Data" button to retrieve the data from the database and display it in a table format.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

