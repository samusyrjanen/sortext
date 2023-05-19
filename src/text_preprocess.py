import string
import re
import nltk
nltk.download('stopwords')

class TextPreprocess:
    def __init__(self, texts: list):
        self.texts = texts
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.stemmer = nltk.stem.PorterStemmer()

    def preprocess(self):
        self.to_lower_case()
        self.remove_punctuation()
        self.numbers_to_num()
        self.split_words()
        self.remove_short_long()
        self.stem()

    def to_lower_case(self):
        self.texts = [text.lower() for text in self.texts]

    def remove_punctuation(self):
        table = str.maketrans('', '', string.punctuation)
        self.texts = [text.translate(table) for text in self.texts]

    def numbers_to_num(self):
        self.texts = [re.sub(r'\d+', 'num', text) for text in self.texts]

    def split_words(self):
        self.texts = [[word for word in text.split() if word not in self.stopwords] for text in self.texts]

    def remove_short_long(self):
        self.texts = [[word for word in text if 2 < len(word) < 21] for text in self.texts]

    def stem(self):
        self.texts = [" ".join([self.stemmer.stem(word) for word in text]) for text in self.texts]

    def get_texts(self):
        return self.texts
