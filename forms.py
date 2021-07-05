from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, ValidationError
from flask_ckeditor import CKEditorField



##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label="Email Address:", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    username = StringField(label="Username:", validators=[DataRequired()])
    submit = SubmitField(label="Create Account")

    # def validate_username(self, email_address_to_check):
    #     email_address = Users.query.filter_by(
    #         email_address=email_address_to_check.data).first()
    #     if email_address:
    #         raise ValidationError('That Email Address already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(label="Email Address:", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


class CommentForm(FlaskForm):
    body = CKEditorField("Comments", validators=[DataRequired()])
    submit = SubmitField(label="SUBMIT COMMENT")