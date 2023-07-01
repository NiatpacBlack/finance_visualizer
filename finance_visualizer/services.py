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


def get_income_data(file_path: str) -> list[tuple[str, str, float, str]]:
    data_frame = pandas.read_excel(file_path, sheet_name='Доходы', skiprows=1, usecols=(0, 1, 3, 9))
    data = data_frame.to_records(index=False)
    return list(data)


def get_expenses_data(file_path: str) -> list[tuple[str, str, float, str]]:
    data_frame = pandas.read_excel(file_path, sheet_name='Расходы', skiprows=1, usecols=(0, 1, 3, 9))
    data = data_frame.to_records(index=False)
    return list(data)


# for column_name in expense_data.columns.ravel():
#     print(expense_data[column_name].tolist())
