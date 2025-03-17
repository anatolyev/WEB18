from flask import jsonify
from flask_restful import abort, Resource
from data import db_session
from data.news import News

def abort_if_news_not_found(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")

class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        return jsonify(
            {
                'news':
                    news.to_dict(only=('title',
                                       'content',
                                       'user_id',
                                       'is_private'))

            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class NewsListResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        return jsonify(
            {
                'news':
                    news.to_dict(only=('title',
                                       'content',
                                       'user_id',
                                       'is_private'))

            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})