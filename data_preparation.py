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
