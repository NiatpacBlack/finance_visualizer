"""This file describes flask-wtf forms for application"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField
from wtforms.validators import DataRequired


class DatePickerForm(FlaskForm):
    date_from = DateField(
        label="Начиная с",
        description="Дата",
        render_kw={"class": "form-control shadow"},
        format='%Y-%m-%d',
        validators=[DataRequired()],
    )
    date_for = DateField(
        label="До",
        description="Дата",
        render_kw={"class": "form-control shadow"},
        format='%Y-%m-%d',
        validators=[DataRequired()],
    )
    submit = SubmitField(
        "Получить отчеты",
        render_kw={
            "class": "btn-lg btn-success mt-2",
            "form": "dateForm",
        },
    )
