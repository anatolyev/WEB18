from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    # http://127.0.0.1:8080/
    return "Привет, Flask!"

@app.route('/countdown')
def countdown():
    # http://127.0.0.1:8080/countdown
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append("Пуск!")
    return "<br>".join(countdown_list)


@app.route('/image')
def image():
    # http://127.0.0.1:8080/image
    return f"""<img src='{url_for('static', filename='/images/image.jpg')}'
               alt='Тут должна быть наша любимая сова!'>"""

@app.route('/sample_page')
def sample_page():
    # http://127.0.0.1:8080/sample_page
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" 
    href="{url_for('static', filename='/css/style.css')}">
    <title>Пример веб-страницы</title>
</head>
<body>
<h1>Привет, Яндекс!</h1>
</body>
</html>"""


@app.route('/bootstrap')
def bootstrap():
    # http://127.0.0.1:8080/bootstrap
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>А что это вы тут делаете?</h1>
    <div class="alert alert-success" role="alert">
  А мы тут элементами bootstrap балуемся!
</div>
<button type="button" class="btn btn-warning">Warning</button>
</body>
</html>"""

i = 0
@app.route('/show_i')
def show_i():
    # http://127.0.0.1:8080/show_i
    global i
    i += 1
    return f"Посещение: {i}"


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
