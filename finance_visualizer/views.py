from flask.views import MethodView
from flask import render_template


class MainView(MethodView):

    def get(self):
        from finance_visualizer.models import get_data_for_report_1
        return render_template(
            "main_page.html",
            report_1_data=get_data_for_report_1(),
        )
