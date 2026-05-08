import pyodbc

def connect_db():
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=SHAQUILLA\\SQLEXPRESS;'
            'DATABASE=ApexLogisticsDB;'
            'Trusted_Connection=yes;'
        )
        return connection
    except Exception as e:
        print("Database connection failed!")
        print(e)
