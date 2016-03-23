import collections

import bs4
import requests


def get_word_counts(url):
    r = requests.get(url)
    html = r.text
    visible_text = get_visible_text(html)

    counts = collections.defaultdict(int)
    for word in visible_text.split():
        word = map_word(word)
        counts[word] += 1

    return counts


def get_visible_text(html):
    #http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_text_elements = [elem for elem in texts if is_visible(elem) and not is_whitespace_only(elem)]
    return ' '.join(visible_text_elements)


def is_visible(element):
    if element.parent.name in {'[document]', 'head', 'title', 'meta', 'style', 'script'}:
        return False
    elif isinstance(element, bs4.element.Comment):
        return False
    return True


def is_whitespace_only(s):
    return s.strip() == ''


def map_word(word):
    word = word.lower()
    return word


if __name__ == '__main__':
    url = 'http://en.wikipedia.org/wiki/Parse_tree'
    print(get_word_counts(url))