from flask import Flask, render_template

app = Flask(__name__)
params = {'title': "Домашняя страница сайта",
          'username': 'Анатольев Алёша'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **params)

if __name__ == '__main__':
    print("http://127.0.0.1:8080/")
    app.run(port=8080, host="127.0.0.1")