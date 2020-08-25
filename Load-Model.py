import pickle
import pandas as pd

with open ("cosine_similarity_model", "rb") as f:
    cosine_sim= pickle.load(f)

with open ("smd_dataset", "rb") as f:
    smd= pickle.load(f)


def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

def get_recommendations_with_id(id):
    idx = indices_id[id]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return ids.iloc[movie_indices]

titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

ids = smd['id']
indices_id = pd.Series(smd.index, index=smd['id'])


print(get_recommendations("Good Will Hunting").head(20))
