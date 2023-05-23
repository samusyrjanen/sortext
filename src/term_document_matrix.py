from functools import reduce

class TermDocumentMatrix:
    def unique_words(self, dataset: list):
        unique_words = reduce(lambda x, y: x.union(y), map(set, dataset))
        return unique_words
