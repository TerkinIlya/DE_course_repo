import clickhouse_connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('CH_HOST')
PORT = getenv('CH_PORT')


# Подключение к ClickHouse
def connect_clickhouse(command):
    try:
        client = clickhouse_connect.get_client(host=HOST, port=PORT)
        print("Connected to ClickHouse")
        res = client.command(command)
        print(res)
    except Exception as e:
        print(f"Error connecting to ClickHouse: {e}")


command = '''
           SELECT * FROM employees;
            '''

connect_clickhouse(command)
