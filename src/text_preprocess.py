import string
import re
import nltk
nltk.download('stopwords')

class TextPreprocess:
    '''
    Preprocesses the text data.

    Attributes:
        texts (list): A list of strings, each string being a text document.

    Methods:
        preprocess(): preprocesses the texts applying all the preprocessing functions.
        to_lower_case()
        remove_punctuation()
        numbers_to_num(): changes each number into a 'num'-string.
        split_words(): splits the text documents into a list of words.
        remove_short_long(): removes words with less than 3 of more that 20 characters.
        stem(): stemmes the words into their base form removing any conjugations. Also joins the word lists back into a string.
        get_texts(): returns the texts (list).
    '''

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
