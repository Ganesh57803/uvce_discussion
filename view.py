import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute the .tables command
cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')

# Get the list of tables
tables = cursor.fetchall()

# Print the list of tables and their schemas
for table in tables:
    print(f"Table schema for {table[0]}:")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    for column in columns:
        print(f"{column[1]}: {column[2]} {column[3]} {column[4]}")

# Close the connection
conn.close()