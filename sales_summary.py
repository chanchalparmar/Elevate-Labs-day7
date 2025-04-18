
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# SQL query to get total quantity and revenue per product
query = '''
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''

# Execute the query and load the data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print the DataFrame
print("Sales Summary:")
print(df)

# Plot the revenue per product
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close the connection
conn.close()
