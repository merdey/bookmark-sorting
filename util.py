from collections import defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer


def map_word(word):
    word = word.lower()
    return word


def vectorize_corpus(corpus):
    documents = [d.text for d in corpus.documents]
    tfidf_vectorizer = TfidfVectorizer(
        max_df=0.8, max_features=200000,
        min_df=0.2, stop_words='english',
        use_idf=True, ngram_range=(1,3)
    )

    return tfidf_vectorizer.fit_transform(documents)