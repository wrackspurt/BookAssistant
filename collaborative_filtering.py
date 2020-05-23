import pandas as pd
import numpy as np

from surprise import Dataset, Reader
from surprise import dump
from surprise import SVD


def load_model():
    _, loaded_model = dump.load('svd-model/model.pickle')
    return loaded_model


def get_predictions(uid, ratings_tuples, book_tuples, bids):
    model = load_model()
    res = []
    for b in bids:
        pred = model.predict(uid, b, verbose=False)
        ret = (pred.iid, pred.est)
        res.append(ret)
    res.sort(key=lambda i: i[1], reverse=True)
    result = res[0:25]
    for t in ratings_tuples:
        for r in result:
            if t[0] == r[0] and t[1] == uid:
                result.remove(r)
    result_with_titles = []
    for r in result:
        for b in book_tuples:
            if r[0] == b[0]:
                result_with_titles.append(b[1])
    return result_with_titles
