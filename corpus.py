class Corpus:
    def __init__(self, documents=None):
        if documents:
            self.documents = documents
        else:
            self.documents = []

        self._cached_tf_idf_vectors = {}

    def add_document(self, doc):
        self.documents.appends(doc)

    def document_frequency(self, word):
        return sum([word in doc for doc in self.documents])

    def tf_idf(self, document):
        if document not in self._cached_tf_idf_vectors:
            word_counts = document.word_counts
            self._cached_tf_idf_vectors[document] = {
                word: count / self.documents_frequency(word)
                for word, count in word_counts.items()
            }
        return self._cached_tf_idf_vectors[document]



