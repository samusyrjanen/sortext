from functools import reduce
import numpy as np

class TermDocumentMatrix:
    '''
    Handles all the matrix operations, such as creating it and calculating TF-IDF.

    Methods:
        unique_words(dataset: list): Returns a set of unique words in a dataset.
        create_term_document_matrix(dataset: list): Creates a matrix in which the rows represent documents, and columns unique words.
    '''

    def unique_words(self, dataset: list):
        unique_words = reduce(lambda x, y: x.union(y), map(set, dataset))
        return unique_words

    def create_term_document_matrix(self, dataset: list):
        '''
        Creates a matrix in which the rows represent documents, and columns unique words. The matrix is created in a way that ensures
        the correct row-column matches with the titles (document_names and unique_words) and cells (matrix).
        Because of the way the method unique_words(dataset: list) functions, the returned set of words has a different indexing each time.
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
