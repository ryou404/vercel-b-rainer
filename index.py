from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form.get("user", "未提供")  
        pwd = request.form.get("pwd", "未提供")  
        result = f"您輸入的帳號是：{user}; 密碼為：{pwd}"
        return result
    return render_template("account.html")

@app.route("/about")
def me():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick", "郭碩元")  # 改回第二份的預設值
    return render_template("welcome.html", name=user)  # 只傳遞 name 變數

@app.route("/")
def index():
    homepage = "<h1>郭碩元 Python 網頁(時間+8 & 傳值)</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"  # 改回不含 work 參數
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>郭碩元簡介網頁</a><br>"
    return homepage  

@app.route("/mis")
def course():
    return "<h1>郭碩元</h1>"

@app.route("/today")
def today():
    now = datetime.now()  # 改回沒有時區處理
    return render_template("today.html", datetime=str(now))

if __name__ == "__main__":
    app.run(debug=True)  # 啟用 debug 模式
