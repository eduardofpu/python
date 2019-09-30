import psycopg2 as psy

def __open_connect(namedb, userdb, passdb, hostdb):

    try:

        connection = psy.connect(database=namedb, user=userdb, password=passdb, host=hostdb)
        cursor = connection.cursor()

    except Exception as ex:

        print('ERROR: %s' % ex)

    return connection, cursor


def __close_connect(connection):

    try:

        if connection is not None:
            connection.close()

    except Exception as ex:

        print('ERROR: %s' % ex)

    return True


def open_data():

    return __open_connect(database, user, password, host)


def close_data(connection):

    return __close_connect(connection)

def __open__cursor(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def open_cursor(connection, query):

    return __open__cursor(connection, query)

