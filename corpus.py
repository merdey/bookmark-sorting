import collections
import math


class Corpus:
    def __init__(self, documents=None):
        if documents:
            self.documents = documents
        else:
            self.documents = []

        self._cached_tf_idf_vectors = {}

    def add_document(self, doc):
        self.documents.append(doc)
        self._cached_tf_idf_vectors = {}

    def inverse_document_frequency(self, word):
        total, containing_word = 0, 0
        for doc in self.documents:
            if word in doc:
                containing_word += 1
            total += 1
        return math.log(total / containing_word)

    def tf_idf(self, document):
        if document not in self._cached_tf_idf_vectors:
            tf_idf_vector = collections.defaultdict(int)
            for word, freq in document.word_frequencies.items():
                tf_idf_vector[word] = freq * self.inverse_document_frequency(word)
            self._cached_tf_idf_vectors[document] = tf_idf_vector
        return self._cached_tf_idf_vectors[document]

    def document_similarity(self, doc_a, doc_b):
        words = doc_a.word_set | doc_b.word_set
        a_vec = self.tf_idf(doc_a)
        b_vec = self.tf_idf(doc_b)

        numerator, denom_a, denom_b = 0, 0, 0
        for word in words:
            a = a_vec[word]
            b = b_vec[word]
            numerator += (a * b)
            denom_a += a ** 2
            denom_b += b ** 2
        denominator = math.sqrt(denom_a) + math.sqrt(denom_b)

        return numerator / denominator
