import mysql.connector

# Establish database connection
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="dbpython"
)

# Create a cursor object
cursor = db.cursor()

# Define the insert statement
insert_stmt = "INSERT INTO MeterReading (ID, CustomerID, Date, Time, ReadingAmount) VALUES (%s, %s, %s, %s, %s)"

# Define the values to insert
values = ('MR001', 'CH001203008872', '03/19/2023', '2:30 PM', 550)

# Execute the insert statement with the values
cursor.execute(insert_stmt, values)

# Commit the transaction to the database
db.commit()

# Close the database connection
db.close()
