import string
import re
import nltk
nltk.download('stopwords')

class TextPreprocessor:
    '''
    Preprocesses the text data.

    Methods:
        preprocess(texts: list): Preprocesses the texts applying all the preprocessing functions.
        to_lower_case(texts: list): Changes each character to lower case.
        remove_punctuation(texts: list): Removes punctuation and other slash commands.
        numbers_to_num(texts: list): Changes each number into a 'num'-string.
        split_words(texts: list): Splits the text documents into a list of words.
        remove_short_long(texts: list): Removes words with less than 3 or more that 20 characters.
        stem(texts: list): Stemmes the words into their base form removing any conjugations. Also joins the word lists back into a string.
    '''

    def __init__(self):
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.stemmer = nltk.stem.PorterStemmer()

    def preprocess(self, texts: list):
        texts = self.to_lower_case(texts)
        texts = self.remove_punctuation(texts)
        texts = self.numbers_to_num(texts)
        texts = self.split_words(texts)
        texts = self.remove_short_long(texts)
        texts = self.stem(texts)
        return texts

    def to_lower_case(self, texts: list):
        return [text.lower() for text in texts]

    def remove_punctuation(self, texts: list):
        replace_chars = {"\n": " ", "\'": " ", "\\": " ", "\r": " ", "\t": " ", "\b": " ", "\f": " "}
        slash_table = str.maketrans(replace_chars)
        punctuation_table = str.maketrans('', '', string.punctuation)

        return [text.translate(slash_table).translate(punctuation_table) for text in texts]

    def numbers_to_num(self, texts: list):
        return [re.sub(r'\d+', 'num', text) for text in texts]

    def split_words(self, texts: list):
        return [[word for word in text.split() if word not in self.stopwords] for text in texts]

    def remove_short_long(self, texts: list):
        return [[word for word in text if 2 < len(word) < 21] for text in texts]

    def stem(self, texts: list):
        return [" ".join([self.stemmer.stem(word) for word in text]) for text in texts]
