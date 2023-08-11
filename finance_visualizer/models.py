"""This file contains the logic of interaction between the application and the database."""
import os
from dotenv import load_dotenv

from typing import Literal

from finance_visualizer.db_client.db import PostgresClient


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


def insert_monefy_data_in_db(data: list[dict]) -> None:
    for row in data:
        if row['amount'] > 0:
            pg_client.insert_in_table(
                table_name='income',
                date_created=row['date'],
                category=row['category'],
                sum=row['amount'],
                comment=row['description']
            )
        if row['amount'] < 0:
            pg_client.insert_in_table(
                table_name='expense',
                date_created=row['date'],
                category=row['category'],
                sum=abs(row['amount']),
                comment=row['description']
            )


if __name__ == '__main__':
    create_all_table()
