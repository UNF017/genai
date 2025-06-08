import gensim.downloader as api
model = api.load("word2vec-google-news-300")
queen_vector = model.get_vector("king") - model.get_vector("man") + model.get_vector("woman")
similar_words = model.similar_by_vector(queen_vector, topn=1)
print(similar_words)
if "actor" in model.key_to_index:
    actor_vector = model.get_vector("actor") - model.get_vector("man") + model.get_vector("woman")
    similar_words = model.similar_by_vector(actor_vector, topn=5)
    print(similar_words)
else:
    print("Word 'actor' not found in the model vocabulary.")
