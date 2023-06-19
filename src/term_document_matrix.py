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
        reduce_word_to_index(word_to_index: dict, important_terms: np.ndarray): Modifies the 'word_to_index' dictionary retaining the important terms.
        get_highest_column_per_row(matrix: np.ndarray): Returns an array of column indices that have the highest TF-IDF value in a given row.
        get_most_frequent_terms(term_document_matrix: np.ndarray, highest_column_per_row: np.ndarray): Returns an array of indices of the most
        frequent terms in the matrix.
        reduce_terms(matrix: np.ndarray, word_to_index: dict, max_terms: int=100): Creates a copy of the TF-IDF matrix with reduced columns, retaining
        only the most important terms.
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
        same dataset. The indexing of documents is still identical and correct every time.

        Args:
            dataset (list): A list of lists, containing the words.

        Returns:
            matrix (np.ndarray): A numpy array, where the rows represent documents, and columns unique words.
            document_names (list): A list of document names (for example "Documet 1").
            unique_words (set): A set of unique words representing the columns in the matrix.
            word_to_index (dict): A dictionary that has words as keys and their indices as values.
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
        return matrix, document_names, unique_words, word_to_index

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

    def reduce_word_to_index(self, word_to_index: dict, important_terms: np.ndarray):
        '''
        Modifies the 'word_to_index' dictionary retaining the important terms in the correct order.

        Returns:
            reduced_word_to_index (dict): A reduced version of the 'word_to_index' dictionary.
        '''

        filtered_dict = {key: value for key, value in word_to_index.items() if value in important_terms}
        sorted_dict = {k: v for k, v in sorted(filtered_dict.items(), key=lambda item: item[1])}
        reduced_word_to_index = {}
        index = 0
        for key in sorted_dict.keys():
            reduced_word_to_index[key] = index
            index += 1
        return reduced_word_to_index

    def get_highest_column_per_row(self, matrix: np.ndarray):
        '''
        Returns an array of column indices that have the highest TF-IDF value in a given row. No duplicates.
        '''

        copy_matrix = np.copy(matrix)
        num_rows = copy_matrix.shape[0]
        selected_cols = np.empty(num_rows, dtype=int)
        selected_cols.fill(-1)
        for i in range(num_rows):
            row = copy_matrix[i]
            max_col = np.argmax(row)

            # Check if the selected column has already been chosen
            while np.any(selected_cols == max_col):
                row[max_col] = -1
                max_col = np.argmax(row)

            selected_cols[i] = max_col
        return selected_cols

    def get_most_frequent_terms(self, term_document_matrix: np.ndarray, highest_column_per_row: np.ndarray):
        '''
        Returns an array of indices of the most frequent terms in the matrix. Indices that are already in highest_column_per_row gets deleted.

        Returns:
            sorted_remaining_term_frequencies (np.ndarray): An array of term indices sorted by highest frequency.
        '''

        term_frequencies = np.sum(term_document_matrix, axis=0)
        term_frequencies[highest_column_per_row] = -1

        #Array of term indices sorted by highest frequency
        sorted_term_frequencies = np.argsort(term_frequencies)[::-1]
        sorted_remaining_term_frequencies = sorted_term_frequencies[:-len(highest_column_per_row)]

        return sorted_remaining_term_frequencies

    def reduce_terms(self, matrix: np.ndarray, word_to_index: dict, term_document_matrix: np.ndarray, max_terms: int):
        '''
        Creates a copy of the TF-IDF matrix with reduced columns, retaining only the most important terms.
        Also creates a copy of the 'word_to_index' to match the reduced matrix. The order of columns is retained.

        Args:
            matrix (np.ndarray): TF-IDF matrix.
            word_to_index (dict): A dictionary that has words as keys and their matrix indices as values.
            max_terms (int): The wanted number of terms to be retained in the new reduced matrix.

        Returns:
            reduced_matrix (np.ndarray): A modified copy of the TF-IDF matrix that only has the wanted number of the most important terms.
            reduced_word_to_index (dict): A modified copy of the 'word_to_index' that only has the wanted number of the most important terms.
        '''

        #Creates an array of the most important terms. values are indices and they are sorted by importance.
        highest_column_per_row = self.get_highest_column_per_row(matrix)
        most_frequent_terms = self.get_most_frequent_terms(term_document_matrix, highest_column_per_row)
        important_terms = np.concatenate((highest_column_per_row, most_frequent_terms), axis=0)

        #Selects the wanted number of terms
        reduced_important_terms = important_terms[:max_terms]

        #Sorts the selected terms by index to retain the original order of the matrix
        sorted_reduced_important_terms = np.sort(reduced_important_terms)

        reduced_matrix = matrix[:, sorted_reduced_important_terms].copy()
        reduced_word_to_index = self.reduce_word_to_index(word_to_index, sorted_reduced_important_terms)
        return reduced_matrix, reduced_word_to_index
