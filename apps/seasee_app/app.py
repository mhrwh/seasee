# Flaskクラスをimportする
from flask import Flask, render_template

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    
    return render_template("index.html")

@app.route('/prefectures/<prefecture_id>')
def prefecture(prefecture_id):
    if prefecture_id=='JP-01':
        text = '北海道'
    else:
        text = 'でーたがありません'
            
    return render_template("prefecture.html", text=text)    

