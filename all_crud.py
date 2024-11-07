import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def insert_row():
    query = """insert into phones(make, model, price, ram, memory) values('samsung', 's25 pro', 153000, 12, 1024)"""

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        my_cursor.execute(query)
        connection.commit()
        print('Row inserted')
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while inserting the row')
    except:
        print('database disconnection failed')

insert_row()

import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def read_user_data():
    make = input('Enter the phone company name: ')
    model = input('Enter the phone model name: ')
    price = float(input('Enter the phone price: '))
    ram = int(input('Enter the phone RAM size: '))
    memory = int(input('Enter the phone Disk size: '))
    return (make, model, price, ram, memory)

def insert_row():
    query = """insert into phones(make, model, price, ram, memory) values(%s, %s, %s, %s, %s)"""

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        phone = read_user_data()
        my_cursor.execute(query, phone)
        connection.commit()
        print('Row inserted')
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while inserting the row')
    except:
        print('database disconnection failed')

insert_row()

import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def list_all_rows():
    query = 'select * from phones'

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query)
        if numberOfRows == 0:
            print('No rows were retrieved from phones')
        else:
            rows = my_cursor.fetchall()
            print('ID   MAKE      MODEL          PRICE     RAM-SIZE  MEMORY')
            print('-' * 56)
            for row in rows:
                print('%-4d %-9s %-14s %-9.1f %-9d %d'%(row[0], row[1], row[2], row[3], row[4], row[5]))
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

list_all_rows()

import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def search_row():
    query = 'select * from phones where id = %s'
    id = int(input('Enter Id to search the phone: '))

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query, id)
        if numberOfRows == 0:
            print(f'phone with Id={id} was not found')
        else:
            row = my_cursor.fetchone()
            print('ID   MAKE      MODEL          PRICE     RAM-SIZE  MEMORY')
            print('-' * 56)
            print('%-4d %-9s %-14s %-9.1f %-9d %d'%(row[0], row[1], row[2], row[3], row[4], row[5]))
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

search_row()
# the search_row function will run

import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def update_row():
    query = 'update phones set price = %s where id = %s'
    phone_id = int(input('Enter Id of the phone to be updated: '))
    new_price = float(input('Enter new price of the phone: '))
    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query, (new_price, phone_id))
        if numberOfRows == 0:
            print(f'phone with Id={phone_id} was not found')
        else:
            print(f'phone with Id={phone_id} was updated')
        my_cursor.close()
        connection.commit()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

update_row()


import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def list_all_rows():
    query = 'select * from phones'

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query)
        if numberOfRows == 0:
            print('No rows were retrieved from phones')
        else:
            rows = my_cursor.fetchall()
            print('ID   MAKE      MODEL          PRICE     RAM-SIZE  MEMORY')
            print('-' * 56)
            for row in rows:
                print('%-4d %-9s %-14s %-9.1f %-9d %d'%(row[0], row[1], row[2], row[3], row[4], row[5]))
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

list_all_rows()
