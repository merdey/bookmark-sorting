import collections

from util import map_word


class Document:
    def __init__(self, text):
        self.words = text.split()
        self.word_set = set(self.words)
        self.num_words = len(self.words)

        self._cached_word_counts = None
        self._cached_word_frequencies = None

    @property
    def word_counts(self):
        if not self._cached_word_counts:
            counts = collections.defaultdict(int)
            for word in self.words:
                w = map_word(word)
                counts[w] += 1

            self._cached_word_counts = counts
        return self._cached_word_counts

    @property
    def word_frequencies(self):
        if not self._cached_word_frequencies:
            self._cached_word_frequencies = {
                word: count / self.num_words
                for word, count in self.word_counts.items()
            }
        return self._cached_word_frequencies

    def __contains__(self, item):
        return bool(self.word_counts[item])