import unittest
from text_preprocess import TextPreprocess

class TestTextPreprocess(unittest.TestCase):
    def setUp(self):
        self.texts = ['To create a function in a class that outputs self.texts, you can define a method within the class that returns the value of the self.texts attribute.',
                      'n this example, the class MyClass has an __init__ method that initializes the self.texts attribute with a value passed as an argument. The get_texts method is defined to 100 times retrieve the value of self.texts and return it.',
                      'testing numbers: 123 1. 44, 45, and 46.']
        self.text_preprocess = TextPreprocess(self.texts)
        
    def test_to_lower_case(self):
        correct = ['to create a function in a class that outputs self.texts, you can define a method within the class that returns the value of the self.texts attribute.',
                   'n this example, the class myclass has an __init__ method that initializes the self.texts attribute with a value passed as an argument. the get_texts method is defined to 100 times retrieve the value of self.texts and return it.',
                   'testing numbers: 123 1. 44, 45, and 46.']
        self.text_preprocess.to_lower_case()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_remove_punctuation_removes_punctuation(self):
        correct = ['To create a function in a class that outputs selftexts you can define a method within the class that returns the value of the selftexts attribute',
                   'n this example the class MyClass has an init method that initializes the selftexts attribute with a value passed as an argument The gettexts method is defined to 100 times retrieve the value of selftexts and return it',
                   'testing numbers 123 1 44 45 and 46']
        self.text_preprocess.remove_punctuation()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_remove_punctuation_removes_slash_commands(self):
        texts = ['To create a function in a\' clas\'s that outputs self.texts, \nyou',
                 '123\n4']
        correct = ['To create a function in a  clas s that outputs selftexts  you',
                 '123 4']
        slash_preprocess = TextPreprocess(texts)
        slash_preprocess.remove_punctuation()
        self.assertEqual(slash_preprocess.get_texts(), correct)

    def test_numbers_to_num(self):
        correct = ['To create a function in a class that outputs self.texts, you can define a method within the class that returns the value of the self.texts attribute.',
                   'n this example, the class MyClass has an __init__ method that initializes the self.texts attribute with a value passed as an argument. The get_texts method is defined to num times retrieve the value of self.texts and return it.',
                   'testing numbers: num num. num, num, and num.']
        self.text_preprocess.numbers_to_num()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_split_words(self):
        correct = [['To', 'create', 'function', 'class', 'outputs', 'self.texts,', 'define', 'method', 'within', 'class', 'returns', 'value', 'self.texts', 'attribute.'],
                   ['n', 'example,', 'class', 'MyClass', '__init__', 'method', 'initializes', 'self.texts', 'attribute', 'value', 'passed', 'argument.', 'The', 'get_texts', 'method', 'defined', '100', 'times', 'retrieve', 'value', 'self.texts', 'return', 'it.'],
                   ['testing', 'numbers:', '123', '1.', '44,', '45,', '46.']]
        self.text_preprocess.split_words()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_remove_short_long(self):
        correct = [['create', 'function', 'class', 'outputs', 'self.texts,', 'define', 'method', 'within', 'class', 'returns', 'value', 'self.texts', 'attribute.'],
                   ['example,', 'class', 'MyClass', '__init__', 'method', 'initializes', 'self.texts', 'attribute', 'value', 'passed', 'argument.', 'The', 'get_texts', 'method', 'defined', '100', 'times', 'retrieve', 'value', 'self.texts', 'return', 'it.'],
                   ['testing', 'numbers:', '123', '44,', '45,', '46.']]
        self.text_preprocess.split_words()
        self.text_preprocess.remove_short_long()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_stem(self):
        correct = ['to creat function class output self.texts, defin method within class return valu self.text attribute.',
                   'n example, class myclass __init__ method initi self.text attribut valu pass argument. the get_text method defin 100 time retriev valu self.text return it.',
                   'test numbers: 123 1. 44, 45, 46.']
        self.text_preprocess.split_words()
        self.text_preprocess.stem()
        self.assertEqual(self.text_preprocess.get_texts(), correct)

    def test_preprocess(self):
        correct = ['creat function class output selftext defin method within class return valu selftext attribut',
                   'exampl class myclass init method initi selftext attribut valu pass argument gettext method defin num time retriev valu selftext return',
                   'test number num num num num num']
        self.text_preprocess.preprocess()
        self.assertEqual(self.text_preprocess.get_texts(), correct)
