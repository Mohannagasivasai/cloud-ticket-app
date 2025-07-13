from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_seats', methods=['POST'])
def select_seats():
    name = request.form['name']
    email = request.form['email']
    movie = request.form['movie']
    showtime = request.form['showtime']
    return render_template('seats.html', name=name, movie=movie, showtime=showtime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
