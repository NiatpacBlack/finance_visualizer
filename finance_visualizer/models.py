import os
from dotenv import load_dotenv

from typing import Literal

from db_client.db import PostgresClient


load_dotenv()

pg_client = PostgresClient(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
)


def create_income_table():
    pg_client.create_table(
        "income",
        """
        id SERIAL PRIMARY KEY,
        date_created date NOT NULL,
        category VARCHAR(255) NOT NULL,
        sum NUMERIC(10, 2) NOT NULL,
        comment VARCHAR(1024) NULL
        """,
    )


def create_expense_table():
    pg_client.create_table(
        "expense",
        """
        id SERIAL PRIMARY KEY,
        date_created date NOT NULL,
        category VARCHAR(255) NOT NULL,
        sum NUMERIC(10, 2) NOT NULL,
        comment VARCHAR(1024) NULL
        """,
    )


def create_all_table():
    create_income_table()
    create_expense_table()


def insert_data_in_db(table_name: Literal['income', 'expense'], data: list[tuple[str, str, float, str]]) -> None:
    insert_query = f"INSERT INTO {table_name} VALUES (date_created, category, sum, comment)"
    with pg_client.db_connect.cursor() as cursor:
        cursor.executemany(insert_query, data)
        pg_client.db_connect.commit()


if __name__ == '__main__':
    from finance_visualizer.config import FILE_PATH
    from services import get_income_data, get_expenses_data
    create_all_table()
    insert_data_in_db('expense', get_expenses_data(FILE_PATH))
    insert_data_in_db('income', get_income_data(FILE_PATH))


