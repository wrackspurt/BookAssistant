import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split


def preparing_data(ratings):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings[['book_id', 'user_id', 'rating']], reader)
    return data


def training(data):
    train_set, test_set = train_test_split(data, test_size=0.2)
    model = SVD(n_factors=80, n_epochs=20, lr_all=0.005, reg_all=0.2)
    model.fit(train_set)
    predictions = model.test(test_set)
    return predictions


def preparing_pred_ds(predictions):
    pred_ds = pd.DataFrame(predictions, columns=['book_id', 'user_id', 'actual_rating', 'pred_rating', 'details'])
    pred_ds['impossible'] = pred_ds['details'].apply(lambda x: x['was_impossible'])
    pred_ds['pred_rating_round'] = pred_ds['pred_rating'].round()
    pred_ds['abs_err'] = abs(pred_ds['pred_rating'] - pred_ds['actual_rating'])
    pred_ds.drop(['details'], axis=1, inplace=True)
    return pred_ds


def get_collaborative_filtering_recs(pred_ds, ratings_titles, id_user):
    ratings_titles = ratings_titles.merge(pred_ds[['book_id', 'user_id', 'pred_rating']],
                                          on=['book_id', 'user_id'], how='left')
    user_ds = ratings_titles[ratings_titles['user_id'] == id_user]
    res_ds = user_ds[user_ds['pred_rating'].notna()].sort_values('rating', ascending=False)
    return res_ds


def prepare_recs(results):
    recs = []
    titles_ds = results['title'].dropna()
    for t in titles_ds:
        recs.append(t)
    return recs
