import math

#used for computing idf by keeping a list of documents
#and the # of docs a word appears in
class Corpus:
    def __init__(self, documents=[]):
        self.documents = documents
        
        #keeps track of how many documents corpus_counts[word] appears in
        self.corpus_counts = {}
        for doc in self.documents:
            for word in doc.word_counts:
                if word in self.corpus_counts:
                    self.corpus_counts[word] += 1
                else:
                    self.corpus_counts[word] = 1

    def addDocument(self, document):
        self.documents.append(document)
        for word in document.word_counts.keys():
            if word in self.corpus_counts:
                self.corpus_counts[word] += 1
            else:
                self.corpus_counts[word] = 1

    def idf(self, word):
        return math.log(len(self.documents) / self.corpus_counts[word])
