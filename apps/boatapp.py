from flask import Flask, render_template, request
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

locations = ['桐　生', '戸　田', '江戸川', '平和島', '多摩川', '浜名湖', '蒲　郡', '常　滑', '　津　', '三　国', 'びわこ', '住之江',
            '尼　崎', '鳴　門', '丸　亀', '児　島', '宮　島', '徳　山', '下　関', '若　松', '芦　屋', '福　岡', '唐　津', '大　村']
#locations = ['location A', 'location B', 'location C', 'location D']
races = ['race A', 'race B', 'race C', 'race D']
# トップページへのルーティング
@app.route('/')
def index():
    # index.htmlをレンダリングして返す
    #locations = ['location A', 'location B', 'location C', 'location D']
    #races = ['race A', 'race B', 'race C', 'race D']
    return render_template('digicon_moc.html', locations=locations, races=races, boat_numbers=None, race_conditions=None)

@app.route('/predict', methods=['POST'])
def predict():
# フォームからlocationとraceの値を取得
    location = request.form.get('location')
    race = request.form.get('race')
    print(location)
    print(race)
    race_conditions = [location, race]
    # 結果を返す
    boat_numbers = [1, 2, 3, 4, 5, 6]
    import random
    boat_numbers = random.sample(boat_numbers, len(boat_numbers))
    #return '予測結果: 会場 = {}, レース = {}'.format(location, race)
    return render_template('digicon_moc.html', locations=locations, races=races, boat_numbers=boat_numbers, race_conditions=race_conditions)


"""
ブループリントの登録
"""
# crudアプリのモジュールviews.pyからBlueprint[crud]をインポート
from apps.crud.views import crud

# FlaskオブジェクトにBlueprint[crud]を登録
app.register_blueprint(crud)