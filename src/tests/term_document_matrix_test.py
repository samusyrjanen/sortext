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

        matrix, document_names, unique_words, word_to_index = self.term_document_matrix.create_term_document_matrix(self.dataset)

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

    def test_compute_idf(self):
        correct = 59.16871558466
        matrix1, do, da, di = self.term_document_matrix.create_term_document_matrix(self.dataset)
        idf = self.term_document_matrix.compute_idf(matrix1)
        idf_sum = np.sum(idf)
        rounded_idf_sum = "{:.11f}".format(idf_sum)
        self.assertEqual(float(rounded_idf_sum), correct)

    def test_create_tfidf_matrix(self):
        correct = 8.58415977128
        matrix1, do, da, di = self.term_document_matrix.create_term_document_matrix(self.dataset)
        tfidf = self.term_document_matrix.create_tfidf_matrix(matrix1)
        tfidf_sum = np.sum(tfidf)
        rounded_tfidf_sum = "{:.11f}".format(tfidf_sum)
        self.assertEqual(float(rounded_tfidf_sum), correct)

    def test_get_important_terms(self):
        correct = 253
        matrix, document_names, unique_words, word_to_index = self.term_document_matrix.create_term_document_matrix(self.dataset)
        tfidf_matrix = self.term_document_matrix.create_tfidf_matrix(matrix)
        important_terms = self.term_document_matrix.get_important_terms(tfidf_matrix)
        self.assertEqual(np.sum(important_terms), correct)

    def test_reduce_word_to_index(self):
        correct = 4
        matrix, document_names, unique_words, word_to_index = self.term_document_matrix.create_term_document_matrix(self.dataset)
        tfidf_matrix = self.term_document_matrix.create_tfidf_matrix(matrix)
        important_terms = self.term_document_matrix.get_important_terms(tfidf_matrix)
        reduced_word_to_index = self.term_document_matrix.reduce_word_to_index(word_to_index, important_terms[:4])
        self.assertEqual(len(reduced_word_to_index), correct)

    def test_reduce_terms(self):
        dict_len = 4
        correct_matrix_sum = 2.2903804
        matrix, document_names, unique_words, word_to_index = self.term_document_matrix.create_term_document_matrix(self.dataset)
        tfidf_matrix = self.term_document_matrix.create_tfidf_matrix(matrix)
        reduced_matrix, reduced_word_to_index = self.term_document_matrix.reduce_terms(tfidf_matrix, word_to_index, 4)
        matrix_sum = np.sum(reduced_matrix)
        rounded_matrix_sum = "{:.7f}".format(matrix_sum)
        self.assertEqual(len(reduced_word_to_index), dict_len)
        self.assertEqual(float(rounded_matrix_sum), correct_matrix_sum)
