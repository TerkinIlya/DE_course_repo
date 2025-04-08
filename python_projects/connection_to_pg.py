from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DATABASE = getenv('PG_DATABASE')
USER = getenv('PG_USER')
PASSWORD = getenv('PG_PASSWORD')
HOST = getenv('PG_HOST')
PORT = getenv('PG_PORT')

connection_string = (
    f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
)


def connect_postgres(sql: str, print_sql=True):
    pg_engine = create_engine(connection_string)
    with pg_engine.begin() as connection:
        result = connection.execute(text(sql))
        if print_sql:
            for row in result:
                print(row)
        else:
            return result


sql = '''
        SELECT * FROM employees
        '''

connect_postgres(sql, print_sql=True)
