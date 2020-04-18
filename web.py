from flask import Flask, render_template, redirect, url_for, request
from data_preparation import get_data_from_csv, get_titles

app = Flask(__name__)

books, ratings, to_read, tags = get_data_from_csv()
titles = get_titles(books)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        option = request.form.get('recType')
        if option == 'content-based-author':
            return redirect(url_for('get_content_based_author'))
        elif option == 'content-based-author-tag':
            return redirect(url_for('get_content_based_author_tag'))
        elif option == 'collaborative-filtering':
            return redirect(url_for('get_collaborative_filtering'))
        elif option == 'popular':
            return redirect(url_for('get_popular_books'))
    return render_template('home.html')


@app.route('/content_based_author', methods=['GET', 'POST'])
def get_content_based_author():
    return render_template('content-based-author.html')


@app.route('/content_based_author_tag', methods=['GET', 'POST'])
def get_content_based_author_tag():
    return render_template('content-based-author-tag.html')


@app.route('/collaborative_filtering', methods=['GET', 'POST'])
def get_collaborative_filtering():
    return render_template('collaborative-filtering.html')


@app.route('/popular_books', methods=['GET', 'POST'])
def get_popular_books():
    return render_template('popular.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
