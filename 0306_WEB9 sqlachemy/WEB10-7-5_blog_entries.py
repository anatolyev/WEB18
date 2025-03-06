from flask import Flask
from data import db_session
from data.news import News
from data.users import User
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()



    # Добавление по id автора
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()

    # Добавление по объекту класса User:
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()


    # Добавление по взаимодействию с записями User в таблице News:
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Личная запись", content="Эта запись личная",
                is_private=True)
    user.news.append(news)
    db_sess.commit()


    # Далее идет обход списка всех новостей:
    # но перед обходом нужно тоже обновить метод __repr__

    # Если хотим получить все новости всех пользователей:
    users = db_sess.query(User).all()

    for user in users:
        for news in user.news:
            print(news)

if __name__ == '__main__':
    main()

