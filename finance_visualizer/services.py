import datetime

import pandas

from dataclasses import dataclass


@dataclass
class CountRubPerMonth:
    jan: float
    feb: float
    mar: float
    apr: float
    may: float
    jun: float
    jul: float
    aug: float
    sep: float
    oct: float
    nov: float
    dec: float


report_1 = {}


def get_income_data(file_path: str) -> list[tuple[datetime.date, str, float, str]]:
    data_frame = pandas.read_excel(file_path, sheet_name='Income', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(data_frame.to_dict('records'))
    return data


def get_expenses_data(file_path: str) -> list[tuple[datetime.date, str, float, str]]:
    data_frame = pandas.read_excel(file_path, sheet_name='Expenses', skiprows=1, usecols=(0, 1, 3, 9))
    data = _convert_str_date_to_datetime(data_frame.to_dict('records'))
    return data


def _convert_str_date_to_datetime(data: dict | list[dict]) -> list[tuple[datetime.date, str, float, str]]:
    result = []
    for el in data:
        date_str = el['Date and time']
        date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y')
        el['Date and time'] = date_obj.date()
        result.append(tuple(el.values()))

    return result


if __name__ == '__main__':
    from finance_visualizer.config import FILE_PATH
    print(get_income_data(FILE_PATH))
    print(get_expenses_data(FILE_PATH))
