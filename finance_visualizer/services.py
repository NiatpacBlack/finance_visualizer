import datetime

import pandas


def get_income_data(file_path: str) -> list[dict]:
    data_frame = pandas.read_excel(file_path, sheet_name='Income', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(list(data_frame.to_dict('records')))
    return data


def get_expenses_data(file_path: str) -> list[dict]:
    data_frame = pandas.read_excel(file_path, sheet_name='Expenses', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(list(data_frame.to_dict('records')))
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


if __name__ == '__main__':
    from finance_visualizer.config import FILE_PATH
    from finance_visualizer.models import insert_data_in_db
    insert_data_in_db('income', get_income_data(FILE_PATH))
    insert_data_in_db('expense', get_expenses_data(FILE_PATH))
