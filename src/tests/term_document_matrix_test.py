import unittest
from term_document_matrix import TermDocumentMatrix

class TestTermDocumentMatrix(unittest.TestCase):
    def setUp(self):
        self.dataset = [['creat', 'function', 'class', 'output', 'selftext', 'defin', 'method', 'within', 'class', 'return', 'valu', 'selftext', 'attribut'],
                        ['exampl', 'class', 'myclass', 'init', 'method', 'initi', 'selftext', 'attribut', 'valu', 'pass', 'argument', 'gettext', 'method', 'defin', 'num', 'time', 'retriev', 'valu', 'selftext', 'return'],
                        ['test', 'number', 'num', 'num', 'num', 'num', 'num']]
        self.term_document_matrix = TermDocumentMatrix()
        
    def test_unique_words(self):
        correct = {'within', 'exampl', 'pass', 'defin', 'valu', 'myclass', 'init', 'function', 'argument', 'retriev', 'selftext', 'output', 'gettext', 'num', 'initi', 'time', 'number', 'method', 'class', 'return', 'creat', 'test', 'attribut'}
        unique_words = self.term_document_matrix.unique_words(self.dataset)
        self.assertEqual(unique_words, correct)
