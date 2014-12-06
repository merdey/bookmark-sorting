from bs4 import BeautifulSoup
from bookmark_conversion import *
from category import *
from document import *
from test import testReadTimings
import nltk, pickle, requests, operator



def printOptions(options):
    print()
    i = 0
    for option in options:
        print('[{0}] {1}'.format(i, option[0]))
        i += 1

def categorizeInput():
    url = input('Enter url: ')

    categorizeSupervised(url)

def categorizeBookmarksSupervised():
    urls_without_save = 0
    for url in unsorted:
        print('Processing ' + url)
        categorizeSupervised(url)
        urls_without_save += 1
        if urls_without_save >= 10:
            response = input('Would you like to save? ')
            if response.lower().startswith('y'):
                save()
                urls_without_save = 0

def categorizeBookmarksUnsupervised():
    urls_without_save = 0
    for url in unsorted:
        print('Processing ' + url)
        categorizeUnsupervised(url)
        urls_without_save += 1
        if urls_without_save >= 10:
            saveToFile('save.txt')
            urls_without_save = 0

def categorizeSupervised(url): #asks user if the category is correct before adding
    doc, matched_category = categorize(url)
    print('Belongs to: ' + matched_category.name)
    response = input('Add to category? ')
    if response.lower().startswith('y'):
        matched_category.update(doc)
        print('Added\n')
    else:
        print('Did not add\n')

def categorizeUnsupervised(url): #automatically adds doc to closest category
    doc, matched_category = categorize(url)
    matched_category.update(doc)

def categorize(url):
    doc = documentFromUrl(url)
    distances = {}
    for category in categories:
        distances[category] = distance(doc, category.corpus, corpus)

    matched_category = min(distances.items(), key=operator.itemgetter(1))[0]
    return doc, matched_category
                
def createNewCategory():
    name = input('Enter category name: ')
    categories.append(Category(name))

def editCategory():
    i = 0
    for category in categories:
        print('[{0}] {1}'.format(i, category.name))
        i += 1
    category = categories[int(input('Select category: '))]

    print('[0] Add document')
    print('[1] Remove document')
    print('[2] List documents')
    response = input('Choose an option: ')
    if response == '0':
        url = input('Enter url: ')
        doc = documentFromUrl(url)
        category.update(doc)
    elif response == '1':
        category.listDocuments()
        d = category.documents[int(input('Document to remove? '))]
        category.remove(d)
    elif response == '2':
        category.listDocuments()
    else:
        print('invalid input')

def save():
    filename = input('Save as? ')
    saveToFile(filename)

def saveToFile(filename):
    save_dict = {'corpus': corpus,
                 'categories': categories,
                 'unsorted': unsorted
                 }
    with open(filename, 'wb') as f:
        pickle.dump(save_dict, f)
        
def load():
    filename = input('Filename? ')
    with open(filename, 'rb') as f:
        load_dict = pickle.load(f)
    return load_dict['corpus'], load_dict['categories'], load_dict['unsorted']

def endProgram():
    global running
    running = False

if __name__ == '__main__':
    testReadTimings(5, 10)
    load_response = input('Load from file? ')
    if load_response.lower().startswith('y'):
        corpus, categories, unsorted = load()
    else:
        #creates categories with predefined documents
        category_definitions = {'Python': ['https://www.python.org/',
                                            'http://en.wikipedia.org/wiki/Python_(programming_language)',
                                            'http://learnpythonthehardway.org/book/'
                                            ],
                                'Gaming': ['http://kotaku.com/',
                                            'http://www.gamespot.com/',
                                            'http://www.ign.com/'
                                            ]
                                }
        categories = []
        for category_name, urls in category_definitions.items():
            category_docs = []
            for url in urls:
                print('reading ' + url)
                category_docs.append(documentFromUrl(url))
            categories.append(Category(category_name, category_docs))
        unsorted = bookmarksToUrls('Profile 1')[100:200]
        print('read in bookmarks')


    options = [('Categorize a url', categorizeInput),
               ('Create new category', createNewCategory),
               ('Edit category', editCategory),
               ('Categorize bookmarks (supervised)', categorizeBookmarksSupervised),
               ('Categorize bookmarks (unsupervised)', categorizeBookmarksUnsupervised),
               ('Save', save),
               ('Quit', endProgram)
               ]
    running = True
    while(running):
        printOptions(options)
        response = int(input('Choose an option: '))
        if response < len(options):
            action = options[response][1]
            action()
        else:
            print('invalid input')
