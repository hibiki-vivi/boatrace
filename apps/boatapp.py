from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flaskのインスタンスを生成
app = Flask(__name__)


# 設定ファイルを読み込む
app.config.from_pyfile('settings.py')

# SQLAlchemyのインスタンスを生成
db = SQLAlchemy()

# Migrateオブジェクトを生成してFlaskオブジェクトとSALAlchemyオブジェクトを登録
Migrate(app, db)

# トップページへのルーティング
@app.route('/')
def index():
    # index.htmlをレンダリングして返す
    return render_template('digicon_moc.html')