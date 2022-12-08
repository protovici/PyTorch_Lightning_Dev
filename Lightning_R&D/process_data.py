import pandas as pd

df = pd.read_csv(r'E:\random_data\in\coffee_maker.csv')
df_new = df.drop(columns=['review_date', 'handle','helpfulness_rating'], axis=1)
def group_ratings(a):

    if a['rating'] <= 3:
        return '0'

    else:
        return '1'

df_new['target'] = df_new.apply(group_ratings, axis = 1)
df_for_model = df_new.drop(columns=['rating'], axis=1)
df_for_model = df_for_model.dropna()
df_for_model.to_csv(r'E:\random_data\in\coffee_maker_ratings.csv', index=False)