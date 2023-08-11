"""This file describes the business logic of the application."""
import datetime

import pandas


def get_income_data(file_path: str) -> list[dict]:
    """
    Takes as input the path to an Excel file with financial data from financial application.

    Creates a dataframe with income data for only the required columns:
        Date and time, Category, Amount in default currency, Comment

    The date is converted to datetime format, and then a list of data is returned in the form of dictionaries.
    """
    data_frame = pandas.read_excel(file_path, sheet_name='Income', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(list(data_frame.to_dict('records')))
    return data


def get_expenses_data(file_path: str) -> list[dict]:
    """
    Takes as input the path to an Excel file with financial data from financial application.

    Creates a dataframe with expense data for only the required columns:
        Date and time, Category, Amount in default currency, Comment

    The date is converted to datetime format, and then a list of data is returned in the form of dictionaries.
    """
    data_frame = pandas.read_excel(file_path, sheet_name='Expenses', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(list(data_frame.to_dict('records')))
    return data


def get_monefy_money_data(file_path: str) -> list[dict]:
    """
    Takes as input the path to an Excel file with financial data from Monefy's financial application.

    The data looks like:

    +------------+---------+----------+--------+----------+------------------+----------+-------------+
    | date       | account | category | amount | currency | converted amount | currency | description |
    +============+=========+==========+========+==========+==================+==========+=============+
    | 12/06/2019 | Cash    | Salary   | 450    | USD      | 450              | USD      | Any comment |
    +------------+---------+----------+--------+----------+------------------+----------+-------------+

    Creates a dataframe with data for only the required columns (date, category, amount, description),
    the date is converted to datetime format, and then a list of data is returned in the form of dictionaries.
    """
    data_frame = pandas.read_excel(file_path, usecols=(0, 2, 3, 7))
    data = _convert_monefy_str_datetime_to_datetime(list(data_frame.to_dict('records')))
    return data


def _convert_str_date_to_datetime(data: list[dict]) -> list[dict]:
    """
    Gets a dictionary or a list of dictionaries containing data matching the pattern as input:
    {
        'Date and time': 'July 11, 2023',
        'Category': 'Category name',
        'Amount in default currency': 300.0,
        'Comment': 'Any comment or empty string'
    }
    The function looks up data in the dictionary by the key 'Date and time'
    and converts the data string into a datatime object, then returns the converted data.
    """
    for el in data:
        date_str = el['Date and time']
        date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y')
        el['Date and time'] = date_obj.date()

    return data


def _convert_monefy_str_datetime_to_datetime(data: list[dict]) -> list[dict]:
    """
    Gets a dictionary or a list of dictionaries containing data matching the pattern as input:
    {
        'date': '12/06/2019',
        'category': 'Category name',
        'amount': 300.0,
        'description': 'Any comment or empty string'
    }
    The function looks up data in the dictionary by the key 'date'
    and converts the data string into a datatime object, then returns the converted data.
    """
    for el in data:
        date_str = el['date']
        date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        el['date'] = date_obj.date()

    return data
