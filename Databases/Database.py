import sqlite3

# Function to create tables in the database
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Posts (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        content TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES Users(id)
                    )''')
    conn.commit()

# Function to insert a new user into the Users table
def insert_user(conn, username, email):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Users (username, email) VALUES (?, ?)''', (username, email))
    conn.commit()

# Function to insert a new post into the Posts table
def insert_post(conn, user_id, content):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Posts (user_id, content) VALUES (?, ?)''', (user_id, content))
    conn.commit()

# Function to retrieve all users from the Users table
def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Users''')
    return cursor.fetchall()

# Function to retrieve all posts from the Posts table
def get_all_posts(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Posts''')
    return cursor.fetchall()

# Main function
def main():
    # Connect to the database
    conn = sqlite3.connect('sample.db')
    create_tables(conn)

    # Insert some sample data
    insert_user(conn, 'user1', 'user1@example.com')
    insert_user(conn, 'user2', 'user2@example.com')
    insert_post(conn, 1, 'This is a post by user1')
    insert_post(conn, 2, 'This is a post by user2')

    # Retrieve and print all users
    print("Users:")
    for user in get_all_users(conn):
        print(user)

    # Retrieve and print all posts
    print("\nPosts:")
    for post in get_all_posts(conn):
        print(post)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
