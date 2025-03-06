from flask import Flask
from data import db_session
from data.users import User
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    user = db_sess.query(User).filter(User.id == 1).first()
    print(user)
    user.name = "User One"
    # Нужно импортировать datetime:
    user.created_date = datetime.now()
    db_sess.commit()

if __name__ == '__main__':
    main()

