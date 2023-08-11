"""This file starts the program. Use it to create a datatables of your financial data."""
from finance_visualizer.config import FINANCE_FILE_PATH, MONEFY_FILE_PATH
from finance_visualizer.models import insert_data_in_db, insert_monefy_data_in_db, create_all_table
from finance_visualizer.services import get_monefy_money_data, get_income_data, get_expenses_data


if __name__ == '__main__':
    create_all_table()
    insert_monefy_data_in_db(get_monefy_money_data(MONEFY_FILE_PATH))
    insert_data_in_db('income', get_income_data(FINANCE_FILE_PATH))
    insert_data_in_db('expense', get_expenses_data(FINANCE_FILE_PATH))
