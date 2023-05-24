import unittest
from term_document_matrix import TermDocumentMatrix
import numpy as np

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

    def test_create_term_document_matrix(self):
        correct_unique_words = {'time', 'num', 'method', 'myclass', 'within', 'test', 'number', 'exampl', 'attribut', 'defin', 'class', 'return', 'creat', 'retriev', 'function', 'output', 'valu', 'argument', 'init', 'pass', 'selftext', 'initi', 'gettext'}

        matrix, document_names, unique_words = self.term_document_matrix.create_term_document_matrix(self.dataset)

        row1_zeros = np.count_nonzero(matrix[0] == 0)
        row1_ones = np.count_nonzero(matrix[0] == 1)

        row2_zeros = np.count_nonzero(matrix[1] == 0)
        row2_ones = np.count_nonzero(matrix[1] == 1)

        row3_zeros = np.count_nonzero(matrix[2] == 0)
        row3_ones = np.count_nonzero(matrix[2] == 1)

        self.assertEqual(row1_zeros, 12)
        self.assertEqual(row1_ones, 9)
        self.assertEqual(row2_zeros, 6)
        self.assertEqual(row2_ones, 14)
        self.assertEqual(row3_zeros, 20)
        self.assertEqual(row3_ones, 2)

        self.assertEqual(document_names, ['Document 1', 'Document 2', 'Document 3'])
        self.assertEqual(unique_words, correct_unique_words)
