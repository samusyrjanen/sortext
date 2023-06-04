class Dataset:
    '''
    Handles the dataset.

    Attributes:
        dataset_reader (DatasetReader): Loads the dataset from "datasets" directory.
        text_preprocessor (TextPreprocessor): Preprocesses the dataset.
    
    Methods:
        get_dataset_files(): Returns all available datasets in "datasets" directory.
        read_dataset(file_name): Loads the selected (file_name) dataset. Returns False if not found.
        preprocess(): Preprocesses the loaded dataset.
        get_dataset(): Returns the current dataset.
        create_term_document_matrix(): Creates a matrix in which the rows represent documents, and columns unique words.
        print_matrix(): Prints the matrix.
        create_tfidf_matrix(): Multiplies TF and IDF matrices into TF-IDF matrix, and normalizes it.
        reduce_terms(max_terms): Reduces the number of terms used in the matrix.
        get_unique_words(): Returns all the unique words in the matrix.
        print_reduced_matrix(): Prints the reduced matrix.
        initialize_centroids(number_of_centroids): Initializes the centroids for clusters.
        print_centroids(): Prints an array of centroid coordinates.
        run_k_means(max_iterations: int=5): Runs the K-means algorithm creating clusters.
        print_clusters(): Prints the cluster array. Columns are documents and values clusters.
    '''

    def __init__(self, dataset_reader, text_preprocessor, term_document_matrix, k_means):
        self.dataset = None
        self.matrix = None
        self.document_names = None
        self.unique_words = None
        self.word_to_index = None
        self.reduced_matrix = None
        self.reduced_word_to_index = None
        self.centroid_coordinates = None
        self.distances = None
        self.clusters = None
        self.dataset_reader = dataset_reader
        self.text_preprocessor = text_preprocessor
        self.term_document_matrix = term_document_matrix
        self.k_means = k_means

    def get_dataset_files(self):
        return self.dataset_reader.get_dataset_files()

    def read_dataset(self, file_name):
        self.dataset = self.dataset_reader.read_dataset(file_name)
        if not self.dataset:
            self.dataset = None
            return False
        return True

    def preprocess(self):
        if self.dataset is None:
            return False
        self.dataset = self.text_preprocessor.preprocess(self.dataset)
        return True

    def get_dataset(self):
        return self.dataset

    def create_term_document_matrix(self):
        if self.dataset is None:
            return False
        self.matrix, self.document_names, self.unique_words, self.word_to_index = self.term_document_matrix.create_term_document_matrix(self.dataset)
        return True

    def print_matrix(self):
        if self.matrix is None:
            return False
        print(f'Terms ({len(self.unique_words)}):', self.unique_words)
        for document_name, row in zip(self.document_names, self.matrix):
            print(document_name + ":", row)
        print(f'\nNumber of unique words: {len(self.unique_words)}\n')
        return True

    def create_tfidf_matrix(self):
        if self.matrix is None:
            return False
        self.matrix = self.term_document_matrix.create_tfidf_matrix(self.matrix)
        return True

    def reduce_terms(self, max_terms):
        if self.matrix is None or max_terms >= len(self.unique_words):
            return False
        self.reduced_matrix, self.reduced_word_to_index = self.term_document_matrix.reduce_terms(self.matrix, self.word_to_index, max_terms)
        return True

    def get_unique_words(self):
        return self.unique_words

    def print_reduced_matrix(self):
        if self.reduced_matrix is None:
            return False
        print(f'Terms ({len(self.reduced_word_to_index)}):', self.reduced_word_to_index)
        for document_name, row in zip(self.document_names, self.reduced_matrix):
            print(document_name + ":", row)
        print(f'\nNumber of unique words: {len(self.reduced_word_to_index)}\n')
        return True

    def initialize_centroids(self, number_of_centroids: int):
        if self.reduced_matrix is None:
            if self.matrix is None or number_of_centroids > len(self.matrix):
                return False
            self.centroid_coordinates, self.distances = self.k_means.initialize_centroids(self.matrix, number_of_centroids)
            return True
        if number_of_centroids > len(self.reduced_matrix):
            return False
        self.centroid_coordinates, self.distances = self.k_means.initialize_centroids(self.reduced_matrix, number_of_centroids)
        return True

    def print_centroids(self):
        if self.centroid_coordinates is None:
            return False
        print('Rows are centroids and columns are unique terms (coordinates)\n')
        print(self.centroid_coordinates)
        print('\nRows are centroids and columns are unique terms (coordinates)\n')
        return True

    def run_k_means(self, max_iterations: int=5):
        if self.centroid_coordinates is None:
            return False
        if self.reduced_matrix is None:
            self.centroid_coordinates, self.clusters = self.k_means.run_k_means(self.matrix,
                                                                                self.centroid_coordinates,
                                                                                self.distances,
                                                                                max_iterations)
            return True
        self.centroid_coordinates, self.clusters = self.k_means.run_k_means(self.reduced_matrix,
                                                                            self.centroid_coordinates,
                                                                            self.distances,
                                                                            max_iterations)
        return True

    def print_clusters(self):
        if self.clusters is None:
            return False
        print('Columns represent documents, and values represent the cluster they belong to\n')
        print(self.clusters)
        print('\nColumns represent documents, and values represent the cluster they belong to\n')
        return True
