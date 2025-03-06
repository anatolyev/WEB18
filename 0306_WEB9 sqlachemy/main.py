from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa234rc34c03jecx3eck_309x3'

def main():
    db_session.global_init("db/blog.db")
    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()