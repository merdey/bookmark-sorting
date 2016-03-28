import pandas as pd
from sklearn.cluster import KMeans

from corpus import Corpus
from scrape import create_document_from_url
from util import vectorize_corpus


if __name__ == '__main__':
    urls = [
        'https://en.wikipedia.org/wiki/Tree_(data_structure)',
        'http://en.wikipedia.org/wiki/Parse_tree',
        'https://en.wikipedia.org/wiki/K-means_clustering',
        'http://en.wikipedia.org/wiki/The_Inheritance_of_Loss',
        'http://en.wikipedia.org/wiki/Lewis_turning_point',
    ]

    corp = Corpus()
    for u in urls:
        doc = create_document_from_url(u)
        corp.add_document(doc)

    vec = vectorize_corpus(corp)

    km = KMeans(n_clusters=4)
    km.fit(vec)

    clusters = km.labels_.tolist()
    bookmarks = {'url': urls,  'cluster': clusters}
    frame = pd.DataFrame(bookmarks, index=[clusters], columns=['url', 'cluster'])
    print(frame)