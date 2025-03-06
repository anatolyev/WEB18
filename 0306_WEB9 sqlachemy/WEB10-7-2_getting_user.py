from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    # Получение первого пользователя:
    user = db_sess.query(User).first()
    print(user.name)
    # Пользователь 1

    # Получение всех пользователей:
    for user in db_sess.query(User).all():
        print(user.name)

    print("Фильтр:")
    # Фильтр id>1 а почте не содержит 3.
    for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%3%")):
        print(user.name)
    # <User> 2 Пользователь 2 email2@email.ru

    print("Фильтр ИЛИ:")
    # Фильтр id>1 замена И на ИЛИ.
    for user in db_sess.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
        print(user.name)
    # <User> 2 Пользователь 2 email2@email.ru
    # <User> 3 Пользователь 3 email3@email.ru




if __name__ == '__main__':
    main()

