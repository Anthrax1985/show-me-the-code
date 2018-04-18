from datetime import timedelta
from flask import request, render_template, Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('memo.html', username=request.form['user'])


@app.route('/add_memo', methods=['POST'])
def add_memo():
    memos = [{'info':'wwwwwwwwssssssss', 'content':'ssdsadadadadsadsada'},{'info':'wwwwwwwwssssssss2', 'content':'ssdsadadadadsadsada2'}]
    return render_template('memo.html', memos=memos)


if __name__ == '__main__':
    app.send_file_max_age_default = timedelta(seconds=1)
    app.run(debug=True)