from scrape import create_document_from_url


if __name__ == '__main__':
    urls = [
        'http://en.wikipedia.org/wiki/Parse_tree',
        'http://en.wikipedia.org/wiki/The_Inheritance_of_Loss',
        'http://en.wikipedia.org/wiki/Lewis_turning_point',
    ]

    for u in urls:
        doc = create_document_from_url(u)
        print(doc.word_counts)