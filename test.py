# test_connection.py
import MySQLdb

try:
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        password='Luvp@tel-270705',
        database='employee_management'
    )
    print("✅ MySQL connection successful!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print(f"✅ MySQL version: {version[0]}")
    
    cursor.close()
    conn.close()
    
except MySQLdb.Error as e:
    print(f"❌ MySQL connection failed: {e}")