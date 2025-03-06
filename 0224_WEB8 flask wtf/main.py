import json
from flask import Flask, render_template


app = Flask(__name__)
app.config["SECRET_KEY"] = "1se54tv34234p7'9p;l78234"
params = {'title': "Домашняя страница сайта",
          'username': 'Анатольев Алёша',
          'number': 1501}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **params)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', **params)

@app.route('/news')
def news():
    with open("files/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html',
                           **params,
                           news=news_list)

if __name__ == '__main__':
    print("http://127.0.0.1:8080/")
    print("http://127.0.0.1:8080/odd_even")
    print("http://127.0.0.1:8080/news")
    app.run(port=8080, host="127.0.0.1")