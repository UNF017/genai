import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
def generate_paragraph(seed_word, topn=10):
    try:
        similar_words = [w for w, _ in model.most_similar(seed_word, topn=topn)]
    except KeyError:
        return f"Sorry, '{seed_word}' not found in vocabulary."
    words = [seed_word] + similar_words
    print(words)
    paragraph = (
        f"Let's explore the world of '{seed_word}'. "
        f"Words like {', '.join(similar_words[:-1])}, and {similar_words[-1]} "
        f"often come up in similar contexts. Together, they create a vibrant story full of ideas."
    )
    return paragraph
seed = "computer"
print(generate_paragraph(seed))
