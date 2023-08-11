"""This file describes all project settings and static variables."""
import os
from dotenv import load_dotenv

load_dotenv()

# Variable in which the executable directory of the script is placed
_basedir = os.path.abspath(os.path.dirname(__file__))

FINANCE_FILE_NAME = "finance_data_example.xlsx"

MONEFY_FILE_NAME = "monefy_finance_data_example.xlsx"

MONEFY_FILE_PATH = f'{os.path.join(_basedir, "files")}/{MONEFY_FILE_NAME}'

FINANCE_FILE_PATH = f'{os.path.join(_basedir, "files")}/{FINANCE_FILE_NAME}'

# Data to connect to PostgresQL database
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
