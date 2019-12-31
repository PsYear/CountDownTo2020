from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('count_down.html')

@app.route('/2020')
def happynewyear():
    return render_template('newyear.html')


if __name__ == '__main__':
    app.run()
