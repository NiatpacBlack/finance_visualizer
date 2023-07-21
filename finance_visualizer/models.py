import os
from dotenv import load_dotenv

from typing import Literal

from finance_visualizer.db_client.db import PostgresClient
from psycopg2.extras import NamedTupleCursor

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


def get_data_for_report_1(request_data: dict):
    query = f"""select date_created, category, sum(i.sum) from 
        (select to_char(date_created, 'MM') as date_created, category, income.sum from income
        where date_created >= '{request_data['date_from']}' and date_created <= '{request_data['date_for']}') as i
        group by category, date_created
        order by category, date_created;
    """
    with pg_client.db_connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    result = {}
    for row in data:
        if row.category not in result:
            result[row.category] = {
                '01': 0.0, '02': 0.0, '03': 0.0, '04': 0.0, '05': 0.0, '06': 0.0,
                '07': 0.0, '08': 0.0, '09': 0.0, '10': 0.0, '11': 0.0, '12': 0.0,
            }
        result[row.category][row.date_created] += float(row.sum)
    return result


def get_data_for_report_2(request_data: dict):
    query = f"""select date_created, category, sum(e.sum) from 
        (select to_char(date_created, 'MM') as date_created, category, expense.sum from expense
        where date_created >= '{request_data['date_from']}' and date_created <= '{request_data['date_for']}') as e
        group by category, date_created
        order by category, date_created;
    """
    with pg_client.db_connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    result = {}
    for row in data:
        if row.category not in result:
            result[row.category] = {
                '01': 0.0, '02': 0.0, '03': 0.0, '04': 0.0, '05': 0.0, '06': 0.0,
                '07': 0.0, '08': 0.0, '09': 0.0, '10': 0.0, '11': 0.0, '12': 0.0,
            }
        result[row.category][row.date_created] += float(row.sum)
    return result


if __name__ == '__main__':
    create_all_table()
