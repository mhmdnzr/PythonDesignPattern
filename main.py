import pyodbc as pyodbc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;DATABASE=Denadb;Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT * from Attr")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row)

    cursor.close()
    connection.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
