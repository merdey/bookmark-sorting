import bs4
import pandas as pd
from sklearn.cluster import KMeans

from corpus import Corpus
from scrape import create_document_from_url
from util import vectorize_corpus


def read_bookmarks_from_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()

    soup = bs4.BeautifulSoup(contents, 'html.parser')
    bookmarks_dict = {}
    for heading in soup.find_all('h3'):
        bookmarks_dict[heading.text] = parse_bookmark_list(heading.next_sibling.next_sibling)
    return bookmarks_dict


def parse_bookmark_list(dl):
    title_urls = []
    for dt in dl.find_all('dt'):
        title_urls.append({
            'url': dt.find('a')['href'],
            'title': dt.find('a').text
        })
    return title_urls




if __name__ == '__main__':
    bookmarks = read_bookmarks_from_file('test_bookmarks.html')
    urls = [bm['url'] for bm in bookmarks['Unsorted']]

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
    print(frame.sort_values(by=['cluster']))