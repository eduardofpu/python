from data.resources.conexao1 import open_data, close_data, open_cursor

def execute():

    # CRIANDO A QUERY
    query = """select id,param1,param2,param3 from tabela where customer_id = '1'"""

    try:

        # REALIZANDO A CONEXÃO
        connect = open_data(query)

        # CRIANDO AS COLUNAS
        rows = open_cursor(connect, query)

        for r in rows:
            print(f'id {r[0]} param1 {r[1]} param1 {r[2]} param3 {r[3]}')


    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:

        # FECHANDO A CONEXÃO
        close_data(connect)

def main():

    execute()


if __name__ == '__main__':
    main()
