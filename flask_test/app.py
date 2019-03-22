from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/register/',methods=['POST','GET'])
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()
