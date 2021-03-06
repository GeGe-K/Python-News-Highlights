from flask import render_template
from app import app
from .request import get_news,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #getting news
    news = get_news()
    print(news)
    title = 'WELCOME HOME'
    return render_template('index.html', title = title, news = news)


@app.route('/news/<id>')
def news(id):

    final_articles = get_articles(id)
    return render_template('news.html',final_articles = final_articles )    