from document import Document

class Category:
    def __init__(self, name, documents=[]):
        self.name = name
        self.corpus = Document(name) #Document to track word counts for all documents
        self.documents = documents
        for document in self.documents:
            self.corpus.add(document.word_counts)

    def update(self, new_document):
        self.documents.append(new_document)
        self.corpus.add(new_document.word_counts)
        
    def remove(self, document):
        self.corpus.remove(document.word_counts)
        self.documents.remove(document)

    def listDocuments(self):
        i = 0
        for doc in self.documents:
            print('[{0}] {1}'.format(i, doc.name))
            i += 1
