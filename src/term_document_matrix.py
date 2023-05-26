import math
from functools import reduce
import numpy as np

class TermDocumentMatrix:
    '''
    Handles all the matrix operations, such as creating it and calculating TF-IDF.

    Methods:
        unique_words(dataset: list): Returns a set of unique words in a dataset.
        create_term_document_matrix(dataset: list): Creates a matrix in which the rows represent documents, and columns unique words.
        compute_tf(matrix: np.ndarray): Creates an array of the number of times a word appears in a document divded by the total number
        of words in the document.
        compute_idf(matrix: np.ndarray): Creates an array of the log of the number of documents divided by the number of documents that
        contain a specific word.
        create_tfidf_matrix(matrix: np.ndarray): Multiplies TF and IDF matrices into TF-IDF matrix, and normalizes it.
    '''

    def unique_words(self, dataset: list):
        '''
        Because of the way this method functions, the returned set of words have a different indexing each time.
        '''

        unique_words = reduce(lambda x, y: x.union(y), map(set, dataset))
        return unique_words

    def create_term_document_matrix(self, dataset: list):
        '''
        Creates a matrix in which the rows represent documents, and columns unique words. The matrix is created in a way that ensures
        the correct row-column matches with the titles (document_names and unique_words) and cells (matrix).
        Because of the way the method unique_words(dataset: list) functions, the returned set of words have a different indexing each time.
        Because of this, the created matrices will not be identical (albeit still correct) if the function is run multiple times with the
        same dataset.

        Args:
            dataset (list): A list of lists, containing the words.

        Returns:
            matrix (np.ndarray): A numpy array, where the rows represent documents, and columns unique words.
            document_names (list): A list of document names (for example "Documet 1").
            unique_words (set): A set of unique words representing the columns in the matrix.
        '''

        unique_words = self.unique_words(dataset)
        num_documents = len(dataset)
        num_unique_words = len(unique_words)

        #Creates an array of zeros.
        matrix = np.zeros((num_documents, num_unique_words), dtype=int)

        #Creates a dictionary which maps each unique word to its corresponding index.
        #This ensures the correct term-cell matches.
        word_to_index = {word: index for index, word in enumerate(unique_words)}

        #Counts the occurences of the unique words into the matrix (np.ndarray).
        for i, document in enumerate(dataset):
            for word in document:
                matrix[i, word_to_index[word]] += 1

        document_names = [f'Document {i+1}' for i in range(num_documents)]
        return matrix, document_names, unique_words

    def compute_tf(self, matrix: np.ndarray):
        tf_matrix = matrix.astype(float)
        matrix_shape = matrix.shape
        row_sums = np.sum(tf_matrix, axis=1)
        for row in range(matrix_shape[0]):
            for column in range(matrix_shape[1]):
                tf_matrix[row, column] /= row_sums[row]
        return tf_matrix

    def compute_idf(self, matrix: np.ndarray):
        nonzeros = np.count_nonzero(matrix, axis=0)
        matrix_shape = matrix.shape
        idf_matrix = np.zeros(matrix_shape, dtype=float)
        for column in range(matrix_shape[1]):
            idf_value = math.log(matrix_shape[0] / nonzeros[column])
            idf_matrix[:, column] = idf_value
        return idf_matrix

    def create_tfidf_matrix(self, matrix: np.ndarray):
        tf_matrix = self.compute_tf(matrix)
        idf_matrix = self.compute_idf(matrix)
        tfidf_matrix = np.multiply(tf_matrix, idf_matrix)
        magnitudes = np.linalg.norm(tfidf_matrix, axis=1)
        matrix_shape = tfidf_matrix.shape
        for row in range(matrix_shape[0]):
            for column in range(matrix_shape[1]):
                tfidf_matrix[row, column] /= magnitudes[row]
        return tfidf_matrix
