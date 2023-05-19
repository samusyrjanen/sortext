import string
import re
import nltk
nltk.download('stopwords')

class TextPreprocess:
    def __init__(self, texts: list):
        self.texts = texts
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.stemmer = nltk.stem.PorterStemmer()

    def preprocess(self):#+ delete words with less than 3 letters
        self.to_lower_case()
        self.remove_punctuation()
        self.numbers_to_num()
        self.split_words()
        self.remove_short()
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

    def remove_short(self):
        self.texts = [[word for word in text if 2 < len(word) < 21] for text in self.texts]

    def stem(self):
        self.texts = [" ".join([self.stemmer.stem(word) for word in text]) for text in self.texts]

    def get_texts(self):
        return self.texts
    
texts = ['To create a function in a class that outputs self.texts, you can define a method within the class that returns the value of the self.texts attribute.',
         'n this example, the class MyClass has an __init__ method that initializes the self.texts attribute with a value passed as an argument. The get_texts method is defined to 100 times retrieve the value of self.texts and return it.',
         'testing numbers: 123 1. 44, 45, and 46.']

stemmed = ['creat function class output selftext defin method within class return valu selftext attribut',
           'exampl class myclass init method initi selftext attribut valu pass argument gettext method defin num time retriev valu selftext return',
           'test number num num num num num']
    
text_preprocess = TextPreprocess(texts)
text_preprocess.preprocess()
preprocessed = text_preprocess.get_texts()
print(preprocessed)
