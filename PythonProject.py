import pymysql

def connect_to_database():
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(
            host='localhost',  # Change to your database host
            user='root',       # MySQL username (default is 'root' in WampServer)
            password='',       # MySQL password (leave it empty or set the actual password)
            db='flights',  # Name of your database in PHPMyAdmin
            charset='utf8mb4',  # Character set (if necessary)
            cursorclass=pymysql.cursors.DictCursor  # You can change this as needed
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM flight_info")  # Replace with your SQL query

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()
        connection.close()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_database()
