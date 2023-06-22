"""This file describes all the url paths of the admin panel."""
from flask.blueprints import Blueprint

from finance_visualizer.views import (
    MainView,
)


app_routes = Blueprint(name="application", import_name=__name__)

app_routes.add_url_rule("/", view_func=MainView.as_view("main"))
