import pandas as pd


def get_data_from_csv():
    books = pd.read_csv('books.csv')
    books.replace(to_replace='J.K. Rowling, Mary GrandPré', value='J.K. Rowling', inplace=True)
    ratings, to_read, tags_1, tags_2 = pd.read_csv('ratings.csv'), pd.read_csv('to_read.csv'),\
                                       pd.read_csv('book_tags.csv'), pd.read_csv('tags.csv')
    tags = pd.merge(tags_1, tags_2, left_on='tag_id', right_on='tag_id', how='inner')
    return books, ratings, to_read, tags


def get_titles(books):
    title = books['title']
    titles = []
    for i in title:
        titles.append(i)
    return titles


def get_indices(ds, col):
    return pd.Series(ds.index, index=ds[col])


def get_collection(books, tags):
    books_with_tags = pd.merge(books, tags, left_on='book_id', right_on='goodreads_book_id', how='inner')
    grouped_ds = books_with_tags.groupby('book_id')['tag_name'].apply(' '.join).reset_index()

    books = pd.merge(books, grouped_ds, left_on='book_id', right_on='book_id', how='inner')
    books['collection'] = (pd.Series(books[['authors', 'tag_name']].fillna('').values.tolist()).str.join(' '))

    return books['collection']


def get_books_url(books, book_id):
    titles, urls = [i for i in books], ['https://www.goodreads.com/book/show/' + str(i) for i in book_id]
    books_urls = {titles[i]: urls[i] for i in range(len(titles))}
    return books_urls


def get_results_with_url(books_urls, recommendations):
    return {k: books_urls[k] for k in books_urls if k in recommendations}


def get_popular(ds):
    rated_books = ds.sort_values('ratings_count', ascending=False).head(20).set_index('title')
    popular = []

    for i in rated_books.index:
        popular.append(i)

    return popular
