from flask.views import MethodView
from flask import render_template

from finance_visualizer.config import FILE_PATH
from finance_visualizer.services import get_income_data, get_expenses_data


class MainView(MethodView):
    def get(self):
        return render_template(
            "main_page.html",
            income_data=get_income_data(FILE_PATH),
            expenses_data=get_expenses_data(FILE_PATH),
        )
