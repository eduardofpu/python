# pip3 install psycopg2
# sudo apt-get build-dep python3-psycopg2
# pip install psycopg2
import psycopg2 as psy

def __open_connect(query):

    try:

        connection = psy.connect(
            database='rw_telecom_services',
            user='rw_telecom_services',
            password='67ghXzZup16',
            host='nextel-digital.cgj6o4vje0vr.sa-east-1.rds.amazonaws.com')

        open_cursor(connection,query)


    except Exception as ex:

        print('ERROR: %s' % ex)


    return connection

def __close_connect(connection):

    try:

        if connection is not None:
            connection.close()

    except Exception as ex:

        print('ERROR: %s' % ex)

    return True


def __open__cursor(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def open_data(query):

    return __open_connect(query)


def close_data(connection):

    return __close_connect(connection)


def open_cursor(connection, query):

    return __open__cursor(connection, query)

