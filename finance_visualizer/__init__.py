from flask import Flask

from finance_visualizer.config import FlaskConfig, TEMPLATES_DIR, STATIC_DIR
from finance_visualizer.routes import app_routes


app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.config.from_object(FlaskConfig)
app.register_blueprint(app_routes)
