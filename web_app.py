from flask import Flask, render_template, redirect, url_for, request
from data_preparation import get_data_from_csv, get_titles, get_indices, get_collection, get_popular, get_books_url, \
    get_results_with_url
from content_based import calculate_similarity, get_content_based_recommendation, prepare_recommendations

app = Flask(__name__)

BOOKS, RATINGS, TO_READ, TAGS = get_data_from_csv()
TITLES = get_titles(BOOKS)
INDICES = get_indices(BOOKS, 'title')
COLLECTION = get_collection(BOOKS, TAGS)
BOOKS_URL = get_books_url(BOOKS['title'], BOOKS['book_id'])


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


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


@app.route('/content_based_author')
def get_content_based_author():
    return render_template('content-based-author.html', bookList=TITLES)


@app.route('/content_based_author', methods=['POST'])
def post_author_results():
    book = request.form.get('bookChoice')
    if book not in TITLES:
        book_error = 'please, choose a book to get recommendations'
        return render_template('content-based-author.html', book_error=book_error, bookList=TITLES)
    else:
        results = get_results_with_url(BOOKS_URL, prepare_recommendations(
            get_content_based_recommendation(calculate_similarity(BOOKS['authors']),
                                             BOOKS['title'], INDICES, book), book))
        return render_template('content-based-author.html', results=results, bookList=TITLES, book=book)


@app.route('/content_based_tag')
def get_content_based_author_tag():
    return render_template('content-based-tag.html', bookList=TITLES)


@app.route('/content_based_tag', methods=['POST'])
def post_author_tag_results():
    book = request.form.get('bookChoice')
    if book not in TITLES:
        book_error = 'please, choose a book to get recommendations'
        return render_template('content-based-tag.html', book_error=book_error, bookList=TITLES)
    else:
        results = get_results_with_url(BOOKS_URL, prepare_recommendations(
            get_content_based_recommendation(calculate_similarity(COLLECTION.head(10000)),
                                             BOOKS['title'], INDICES, book), book))
        return render_template('content-based-tag.html', results=results, bookList=TITLES, book=book)


@app.route('/collaborative_filtering', methods=['GET', 'POST'])
def get_collaborative_filtering():
    return render_template('collaborative-filtering.html')


@app.route('/popular_books', methods=['GET', 'POST'])
def get_popular_books():
    popular_books = get_results_with_url(BOOKS_URL, get_popular(BOOKS))
    return render_template('popular.html', popular_books=popular_books)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
