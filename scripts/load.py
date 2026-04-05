# import required libraries
import pandas as pd
import psycopg2

# -----------------------------
# Step 1: Read cleaned dataset
# -----------------------------
# This reads the transformed CSV file created by transform.py
df = pd.read_csv("../data/cleaned_sales.csv")


# -----------------------------
# Step 2: Connect to PostgreSQL
# -----------------------------
# Establish connection to the database
conn = psycopg2.connect(
    host="localhost",      # database host
    database="sales_db",   # database name
    user="postgres",       # postgres username
    password="2304"    # postgres password
)

# Create cursor object to execute SQL queries
cursor = conn.cursor()


# -----------------------------
# Step 3: Insert data into table
# -----------------------------
# Loop through each row of dataframe and insert into database
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO sales_data
        (ordernumber, quantityordered, priceeach, revenue)
        VALUES (%s, %s, %s, %s)
        """,
        (
            row["ORDERNUMBER"],        # order number
            row["QUANTITYORDERED"],    # quantity of product ordered
            row["PRICEEACH"],          # price per item
            row["REVENUE"]             # calculated revenue
        )
    )


# -----------------------------
# Step 4: Save changes
# -----------------------------
# Commit the transaction so data is permanently stored
conn.commit()


# -----------------------------
# Step 5: Close connection
# -----------------------------
# Close cursor and database connection
cursor.close()
conn.close()


# -----------------------------
# Final Message
# -----------------------------
print("Data loaded into database successfully")