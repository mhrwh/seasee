# Flaskクラスをimportする
from flask import Flask, render_template

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    data = [{'prefecture' : '北海道', 'ratio': 0.5, 'beaches': ['白浜海岸海水浴場', '石狩浜海水浴場',]}, {'prefecture' : '青森', 'ratio': 0.75, 'beaches': ['白浜海水浴場']}]
    return render_template("index.html",data=data)

@app.route('/prefectures/<prefecture_id>')
def prefecture(prefecture_id):
    if prefecture_id=='JP-01':
        data = '北海道'
    if prefecture_id=='JP-47':
        data = {'prefecture' : '沖縄', 'beaches': [{'name': '底地ビーチ', 'address': '沖縄県石垣市川平185-1', 'open': True}, {'name': '万座ビーチ', 'address': '沖縄県国頭郡恩納村字瀬良垣2260番地', 'open': False},{'name': '喜瀬ビーチ', 'address': '沖縄県名護市字喜瀬115番地2', 'open': True}]}

    else:
        data = 'でーたがありません'
            
    return render_template("prefecture.html", data=data)    

