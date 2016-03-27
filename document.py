import collections

from util import map_word


class Document:
    def __init__(self, text):
        self.words = text.split()
        self.num_words = len(self.words)
        self._cached_word_counts = None

    def word_frequency(self, word):
        word = map_word(word)
        return self.word_counts.get(word, 0) / self.num_words

    @property
    def word_counts(self):
        if not self._cached_word_counts:
            counts = collections.defaultdict(int)
            for word in self.words:
                w = map_word(word)
                counts[w] += 1

            self._cached_word_counts = counts
        return self._cached_word_counts

    def __contains__(self, item):
        return bool(self.word_counts[item])