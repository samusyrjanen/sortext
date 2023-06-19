import time

class Commands:
    '''
    Functions for all the commands.

    Attributes:
        dataset (Dataset): Dataset class that handles the dataset (dataset.py).

    Methods:
        read_dataset(): Loads a dataset from "datasets" directory.
        preprocess_dataset(): Preprocesses the loaded dataset.
        print_text(): Prints a user-selected text from the dataset.
        create_term_document_matrix(): Creates a matrix where rows are documents and columns are unique words.
        The cells represent the number of occurences of each word.
        print_matrix()
        create_tfidf_matrix(): Calculates the term-document matrix into normalized TF-IDF matrix.
        reduce_terms(): Reduces the terms used for the clustering algorithm.
        print_reduced_matrix(): Prints the reduced matrix.
        initialize_centroids(): Initializes centroids for clusters.
        print_centroids(): Prints an array of centroid coordinates.
        run_k_means(): Runs the K-means algorithm.
        print_clusters(): Prints an array that indicates which clusters each document belongs to. Columns are documents and values clusters.
        print_document_information(): Prints some information of a specific document.
        print_cluster(): Prints a list of documents belonging to a specific cluster.
        input_article(): Creates a .txt file of a user input.
        clear_inputs(): Deletes all user inputs.
        run_all(): Runs all the operations.
    '''

    def __init__(self, dataset):
        self.dataset = dataset

    def read_dataset(self):
        datasets = self.dataset.get_dataset_files()
        print('\n\nDatasets:')
        for file in datasets:
            print(file)
        selected_dataset = input('\nSelect a dataset by writing its name: ')
        start_time = time.time()
        print('Loading...')
        while not self.dataset.read_dataset(selected_dataset):
            print('Not found, try again')
            print('\n\nDatasets:')
            for file in datasets:
                print(file)
            selected_dataset = input('\nSelect a dataset: ')
            start_time = time.time()
            print('Loading...')
        print('Dataset loaded')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Loading time: {elapsed_time} seconds\n')

    def preprocess_dataset(self):
        print('Preprocessing...')
        start_time = time.time()
        if not self.dataset.preprocess():
            print('\nNo dataset, load a dataset first\n')
            return
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done')
        print(f'Preprocessing time: {elapsed_time} seconds\n')

    def print_text(self):
        dataset_texts = self.dataset.get_dataset()
        user_inputs = self.dataset.get_user_inputs()
        if not dataset_texts:
            print('\nNo dataset, load a dataset first\n')
            return
        dataset_length = len(dataset_texts)
        dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                              f'plus {user_inputs} user inputs. The user inputs are located '
                              f'last of all texts (highest indices).\n\n'
                              f'Select an index (1-{dataset_length}): ')
        while True:
            try:
                if 1 <= int(dataset_index) <= dataset_length:
                    print(f'\n{dataset_texts[int(dataset_index)-1]}\n')
                    return
            except:
                pass
            print('Not found')
            dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                                  f'plus {user_inputs} user inputs. The user inputs are located '
                                  f'last of all texts (highest indices).\n\n'
                                  f'Select an index (1-{dataset_length}): ')

    def print_preprocessed_text(self):
        dataset_texts = self.dataset.get_preprocessed_dataset()
        user_inputs = self.dataset.get_user_inputs()
        if not dataset_texts:
            print('\nNo dataset, preprocess a dataset first\n')
            return
        dataset_length = len(dataset_texts)
        dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                              f'plus {user_inputs} user inputs. The user inputs are located '
                              f'last of all texts (highest indices).\n\n'
                              f'Select an index (1-{dataset_length}): ')
        while True:
            try:
                if 1 <= int(dataset_index) <= dataset_length:
                    print(f'\n{dataset_texts[int(dataset_index)-1]}\n')
                    return
            except:
                pass
            print('Not found')
            dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                                  f'plus {user_inputs} user inputs. The user inputs are located '
                                  f'last of all texts (highest indices).\n\n'
                                  f'Select an index (1-{dataset_length}): ')

    def create_term_document_matrix(self):
        start_time = time.time()
        print('Creating a matrix...')
        if not self.dataset.create_term_document_matrix():
            print('\nLoad and preprocess a dataset first\n')
            return
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done')
        print(f'Term-document matrix creation time: {elapsed_time} seconds\n')

    def print_matrix(self):
        if not self.dataset.print_matrix():
            print('\nCreate a matrix first\n')

    def create_tfidf_matrix(self):
        start_time = time.time()
        print('Creating TF-IDF matrix...')
        if not self.dataset.create_tfidf_matrix():
            print('\nCreate a term-document matrix first\n')
            return
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done')
        print(f'TF-IDF matrix creation time: {elapsed_time} seconds\n')

    def reduce_terms(self):
        unique_words = self.dataset.get_unique_words()
        data = self.dataset.get_dataset()
        while True:
            max_terms = input(f'\n\nThere are currently {len(data)} documents, and {len(unique_words)-1} unique terms (columns) in the matrix.'
                              f'\n\nSelect the number of terms to retain ({len(data)}-{len(unique_words)-1}) '
                              '(lower is faster, but higher is more accurate): ')
            start_time = time.time()
            try:
                max_terms = int(max_terms)
            except:
                print('Give an integer')
                continue
            if not self.dataset.reduce_terms(max_terms):
                print('Error, ensure that you have loaded a TF-IDF matrix and the value is not lower '
                      'that the number of documents (rows), or higher than the number '
                      'of unique terms (columns) in the matrix.')
                continue
            break
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done')
        print(f'Term reduction time: {elapsed_time} seconds\n')

    def print_reduced_matrix(self):
        if not self.dataset.print_reduced_matrix():
            print('\nCreate a reduced matrix first\n')

    def initialize_centroids(self):
        while True:
            number_of_centroids = input('\n\nGive number of clusters (lower is faster, but higher is more accurate): ')
            try:
                number_of_centroids = int(number_of_centroids)
            except:
                print('Error: Give an integer\n')
                continue
            start_time = time.time()
            print('Initializing centroids...')
            if self.dataset.initialize_centroids(number_of_centroids):
                end_time = time.time()
                elapsed_time = end_time - start_time
                print('Done')
                print(f'Centroid initialization time: {elapsed_time} seconds\n')
                break
            print('Error: Create TF-IDF matrix first, and give ensure the number of clusters is smaller than the number of documents\n')

    def print_centroids(self):
        if not self.dataset.print_centroids():
            print('Error: Initialize centroids first\n')

    def run_k_means(self):
        while True:
            max_iterations = input('\n\nGive maximum iterations for clustering (usually takes 10-20 iterations for convergence): ')
            try:
                max_iterations = int(max_iterations)
            except:
                print('Error: Maximum iterations must be an integer')
                continue
            break
        start_time = time.time()
        if not self.dataset.run_k_means(max_iterations):
            print('Error: Initialize centroids first\n')
            return
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done')
        print(f'Clustering time: {elapsed_time} seconds\n')

    def print_clusters(self):
        clusters = self.dataset.get_clusters()
        if clusters is None:
            print('Error: Run K-means clustering first\n')
            return
        for index in range(len(clusters)):
            print(f'Document {index+1}: cluster {clusters[index]+1}')
        print()

    def print_document_information(self):
        dataset_texts = self.dataset.get_dataset()
        user_inputs = self.dataset.get_user_inputs()
        if not dataset_texts:
            print('\nNo dataset, load a dataset first\n')
            return
        preprocessed_dataset_texts = self.dataset.get_preprocessed_dataset()
        if not dataset_texts:
            print('\nNo dataset, preprocess a dataset first\n')
            return
        clusters = self.dataset.get_clusters()
        if clusters is None:
            print('Error: Run K-means clustering first\n')
            return
        dataset_length = len(dataset_texts)
        dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                              f'plus {user_inputs} user inputs. The user inputs are located '
                              f'last of all texts (highest indices).\n\n'
                              f'Select an index (1-{dataset_length}): ')
        while True:
            try:
                if 1 <= int(dataset_index) <= dataset_length:
                    print(f'\n{dataset_texts[int(dataset_index)-1]}\n')
                    print(f'Preprocessed document:\n{preprocessed_dataset_texts[int(dataset_index)-1]}\n')
                    print(f'Document {dataset_index} belongs to the cluster {clusters[int(dataset_index)-1]+1}\n')
                    return
            except:
                pass
            print('Not found')
            dataset_index = input(f'\n\nThere are {dataset_length-user_inputs} texts in the dataset, '
                                  f'plus {user_inputs} user inputs. The user inputs are located '
                                  f'last of all texts (highest indices).\n\n'
                                  f'Select an index (1-{dataset_length}): ')

    def print_cluster(self):
        clusters = self.dataset.get_clusters()
        if clusters is None:
            print('Error: Run K-means clustering first\n')
            return
        number_of_clusters = max(clusters) + 1
        cluster_index = input(f'\n\nGive cluster index (1-{number_of_clusters}): ')
        while True:
            try:
                if 1 <= int(cluster_index) <= number_of_clusters:
                    counter = 0
                    for i in range(len(clusters)):
                        if clusters[i] == int(cluster_index)-1:
                            print(f'Document {i+1}')
                            counter += 1
                    print(f'\nTotal number of documents in cluster {cluster_index} is {counter}\n')
                    return
            except:
                pass
            print('Not found')
            cluster_index = input(f'\n\nGive cluster index (1-{number_of_clusters}): ')

    def input_article(self):
        print('\nEnter your article text below. Type "/end" on an empty line to finish:')
        lines = []
        while True:
            line = input()
            if line == '/end':
                break
            lines.append(line)
        text = '\n'.join(lines)
        self.dataset.input_article(text)
        print('\nDone\n')

    def clear_inputs(self):
        self.dataset.clear_inputs()
        print('Done\n')

    def run_all(self):
        self.read_dataset()
        self.preprocess_dataset()
        self.create_term_document_matrix()
        self.create_tfidf_matrix()
        self.reduce_terms()
        self.initialize_centroids()
        self.run_k_means()
