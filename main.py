from corpus import Corpus
from scrape import create_document_from_url


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

    print(corp.document_similarity(corp.documents[0], corp.documents[1]))
    print(corp.document_similarity(corp.documents[0], corp.documents[2]))
    print(corp.document_similarity(corp.documents[1], corp.documents[2]))