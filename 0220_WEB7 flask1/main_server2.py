from flask import Flask, url_for, request

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


@app.route('/parameters/<username>/<int:number>')
def parameters(username, number):
    # http://127.0.0.1:8080/parameters/Пафнутий/12
    return f"""<!doctype html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Параметры</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      </head>
      <body>
        <h1>Параметры адресной строки</h1>
        <div class="alert alert-success" role="alert">
      Привет: {username} тебе {number} лет.
    </div>
    
    </body>
    </html>"""



@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    # http://127.0.0.1:8080/form_sample
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"



if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
