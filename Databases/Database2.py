import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')

# Function to add data to the table
def add_data(name, age):
    cursor.execute('''INSERT INTO my_table (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    print("Data added successfully!")

# Function to delete data from the table
def delete_data(id):
    cursor.execute('''DELETE FROM my_table WHERE id = ?''', (id,))
    conn.commit()
    print("Data deleted successfully!")

# Function to print all data in the table
def print_data():
    cursor.execute('''SELECT * FROM my_table''')
    rows = cursor.fetchall()
#    print("\nID\tName\tAge")
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")

# Adding sample data
add_data('John', 30)
add_data('Alice', 25)
add_data('Bob', 35)

# Print initial data
print("Initial data:")
print_data()

# Deleting a record
delete_data(2)

# Print data after deletion
print("\nData after deletion:")
print_data()

# Close cursor and connection
#cursor.close()
#conn.close()
