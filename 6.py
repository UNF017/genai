import tf_keras as keras
from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
sentences = [
    "I love using Hugging Face models, they are amazing!",
    "The weather today is terrible and I feel so sad.",
    "this phone is good but camera is bad",
    "i have neutral opion",
    "This is the best day of my life!",
    "I'm not sure how I feel about this."
]
results = sentiment_analyzer(sentences)
for sentence, result in zip(sentences, results):
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {result['label']}, Confidence: {result['score']:.4f}")
    print("-" * 50)
