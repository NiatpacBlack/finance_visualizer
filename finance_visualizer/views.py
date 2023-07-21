from flask.views import MethodView
from flask import render_template, request

from finance_visualizer.forms import DatePickerForm
from finance_visualizer.models import get_data_for_report_2


class MainView(MethodView):

    def get(self):
        form = DatePickerForm()
        return render_template(
            "main_page.html",
            form=form,
        )


class ReportsView(MethodView):
    def post(self):
        from finance_visualizer.models import get_data_for_report_1
        request_data = request.form.to_dict()

        return render_template(
            "reports_page.html",
            report_1_data=get_data_for_report_1(request_data),
            report_2_data=get_data_for_report_2(request_data),
        )
