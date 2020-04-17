from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        option = request.form.get('recType')
        if option == 'content-based':
            return redirect(url_for('get_content_based'))
        elif option == 'collaborative-filtering':
            return redirect(url_for('get_collaborative_filtering'))
        elif option == 'popular':
            return redirect(url_for('get_popular_books'))
    return render_template('home.html')


@app.route('/content_based', methods=['GET', 'POST'])
def get_content_based():
    return render_template('content-based.html')


@app.route('/collaborative_filtering', methods=['GET', 'POST'])
def get_collaborative_filtering():
    return render_template('collaborative-filtering.html')


@app.route('/popular_books', methods=['GET', 'POST'])
def get_popular_books():
    return render_template('popular.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
