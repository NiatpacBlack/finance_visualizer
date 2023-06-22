import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from finance_visualizer.config import FILE_PATH


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


def get_income_data(file_path: str) -> DataFrame:
    return pd.read_excel(file_path, sheet_name='Доходы', skiprows=1)


def get_expenses_data(file_path: str) -> DataFrame:
    return pd.read_excel(file_path, sheet_name='Расходы', skiprows=1)


income_data = get_income_data(FILE_PATH)

for column_name in income_data.columns.ravel():
    if column_name == 'Категория':
        for category in income_data[column_name].tolist():
            report_1[category] = CountRubPerMonth(*[0 for _ in range(12)])

print(report_1.items())

# for column_name in expense_data.columns.ravel():
#     print(expense_data[column_name].tolist())
