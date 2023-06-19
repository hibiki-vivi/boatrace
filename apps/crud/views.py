from flask import Blueprint

# 識別名をcrudにしてBlueprintオブジェクトを生成
#
# テンプレートフォルダーは同じディレクトリの'templates'
# staticフォルダーは同じディレクトリの'static_crud'
crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static_crud',
)

"""
管理者画面のルーティングとビューの定義
"""
from flask import render_template, url_for, redirect, session
from apps.crud import forms # apps/crud/forms.pyをインポート
from apps.boatapp import app # apps/blogapp.pyからappをインポート

@crud.route('/admin', methods=['GET', 'POST'])
def login():
    # フォームクラスAdminFormのインスタンスを生成
    form = forms.AdminForm()
    session['logged_in'] = False
    
    # ログイン画面のsubmitボタンがクリックされた時の処理
    if form.validate_on_submit():
        # ログイン画面に入力されたユーザー名とパスワードを
        # settings.pyのUSERNAMEとPASSWORDの値を照合する
        if form.username.data != app.config['USERNAME'] \
        or form.password.data != app.config['PASSWORD']:
            # 認証できない場合は、再度logint.htmlをレンダリングして
            # フォームクラスのインスタンスformを引き渡す
            error = 'ユーザIDもしくはパスワードが間違っています'
            return render_template('login.html', form=form, error=error)
        else:
            # 認証できた場合はsessin['logged_in']をTrueにして
            # 管理者画面にリダイレクトする
            #return redirect(url_for('crud.admin'))
            return render_template('boatadmin.html')
    return render_template('login.html', form=form)