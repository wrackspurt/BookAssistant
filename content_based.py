import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def calculate_similarity(data):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tf_matrix = tf.fit_transform(data)
    cos_sim = linear_kernel(tf_matrix, tf_matrix)
    return cos_sim


def get_content_based_recommendation(titles, indices, similarities, title):
    idx = indices[title]

    sim = list(enumerate(similarities[idx]))
    sim = sorted(sim, key=lambda x: x[1].all(), reverse=True)
    sim = sim[1:22]

    book_indices = [i[0] for i in sim]

    return titles.iloc[book_indices]


def prepare_recommendations(rec_data, title):
    results = []

    for i in rec_data:
        results.append(i)

    for i in results:
        if i == title:
            results.remove(i)

    return results[1:21]
