from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

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
    user = request.values.get("nick")  
    w = request.values.get("work")  # 修正縮排錯誤
    return render_template("welcome.html", name=user, work=w)  # 傳遞 work 變數

@app.route("/")
def index():
    homepage = "<h1>郭碩元 Python 網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang&work=developer>傳送使用者暱稱與工作</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>郭碩元簡介網頁</a><br>"
    return homepage  # 刪除多餘的 return

@app.route("/mis")
def course():
    return "<h1>郭碩元</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime=str(now))

if __name__ == "__main__":
    app.run(debug=True)  # 啟用 debug 模式

