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



if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
