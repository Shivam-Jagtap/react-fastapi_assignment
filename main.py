import csv;
from fastapi import FastAPI,UploadFile
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
conn = sqlite3.connect('fastsqlDatabase.db')
cursor = conn.cursor()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Update with the actual URL of your React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
@app.post('/upload')
async def uploadData(file: UploadFile):
    conn = sqlite3.connect('fastsqlDatabase.db')
    cursor = conn.cursor()

    try:
        # Read the file asynchronously
        csv_data = await file.read()

        # Decode the file data
        csv_data = csv_data.decode("utf-8")

        table_name = file.filename.split(".")[0]
        print("table name is :" + table_name)

        # Creating table for CSV data with columns from the header row
        csv_reader = csv.reader(csv_data.splitlines(), delimiter=",")
        csv_header = next(csv_reader)
        column_names = [column.strip() for column in csv_header]
        column_definitions = ", ".join(f"{name} TEXT" for name in column_names)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        cursor.execute(create_table_query)

        # Inserting data into the table
        insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(column_names))})"
        for row in csv_reader:
            cursor.execute(insert_query, row)

        conn.commit()

        return {"message": "File uploaded successfully"}

    except sqlite3.Error as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

    # return {"data saved into database"}

@app.get('/getData')
async def getDataFromDB():
    conn = sqlite3.connect('fastsqlDatabase.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = [row[0] for row in cursor.fetchall()]

        # data is a map that will map a table with its table name
        data = {}
        for table_name in table_names:
            print(table_name)
            cursor.execute(f"SELECT * FROM {table_name}")
            table_data = cursor.fetchall()
            if(table_name == "sqlite_sequence") :
                continue
            
            data[table_name] = table_data

        return data

    except sqlite3.Error as e:
        # return {"error":str(e)}
        return "You have error in sql"
    
    finally:
        cursor.close()
        conn.close()