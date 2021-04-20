from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, TextAreaField, FileField


class VideoForm(FlaskForm):
    title = StringField('Название видео', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[])
    video = FileField('Видео', validators=[DataRequired()])
    preview = FileField('Обложка', validators=[DataRequired()])
    submit = SubmitField('Загрузить')
