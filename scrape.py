import bs4
import requests

from document import Document


def create_document_from_url(url):
    r = requests.get(url)
    html = r.text
    visible_text = get_visible_text(html)
    return Document(text=visible_text)


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