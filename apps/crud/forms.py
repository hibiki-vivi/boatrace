from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    """ログイン画面のフォームクラス

    Attributes:
        username: ユーザID
        password: パスワード
        submit: 送信ボタン
    """
    username = StringField(
        "ユーザID",
        validators=[DataRequired(message="入力が必要です")]
    )
    password = PasswordField(
        "パスワード",
        validators=[DataRequired(message="入力が必要です")]
    )
    # フォームのsubmitボタン
    submit = SubmitField(("ログイン"))
