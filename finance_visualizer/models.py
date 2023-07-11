import datetime
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


def insert_data_in_db(table_name: Literal['income', 'expense'],
                      data: list[dict]) -> None:
    for row in data:
        pg_client.insert_in_table(
            table_name=table_name,
            date_created=row['Date and time'],
            category=row['Category'],
            sum=row['Amount in default currency'],
            comment=row['Comment']
        )


if __name__ == '__main__':
    from finance_visualizer.config import FILE_PATH
    from services import get_income_data, get_expenses_data
    create_all_table()
    insert_data_in_db('expense', get_expenses_data(FILE_PATH))
    insert_data_in_db('income', get_income_data(FILE_PATH))
