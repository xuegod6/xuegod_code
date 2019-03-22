from  flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')
def index():
    context = {
        'a':1,
        'b':2
    }
    return render_template('index.html',**context)

from models import Article
from flask import render_template
@app.route('/')
def articles():
    articles = Article.select()
    context = {
        'articles':articles
    }
    return render_template('articles.html',articles=articles)

from flask import request
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        request_data = request.form
        try:
            title = request_data['title']
            author = request_data['author']
            time = request_data['time']
            description = request_data['description']
            content = request_data['content']
            article = Article()
            article.title = title
            article.author = author
            article.time = time
            article.description =description
            article.content = content
            article.save()
        except:
            return '500'

    return render_template('register.html')




if __name__ == '__main__':
    app.run()