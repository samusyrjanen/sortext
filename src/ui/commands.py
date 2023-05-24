class Commands:
    '''
    Functions for all the commands.

    Attributes:
        dataset (Dataset): Dataset class that handles the dataset (dataset.py).

    Methods:
        read_dataset(): Loads a dataset from "datasets" directory.
        preprocess_dataset(): Preprocesses the loaded dataset.
        print_text(): Prints a user-selected text from the dataset.
    '''

    def __init__(self, dataset):
        self.dataset = dataset

    def read_dataset(self):
        datasets = self.dataset.get_dataset_files()
        print('\n\nDatasets:')
        for file in datasets:
            print(file)
        selected_dataset = input('\nSelect a dataset: ')
        print('Loading...')
        while not self.dataset.read_dataset(selected_dataset):
            print('Not found, try again')
            print('\n\nDatasets:')
            for file in datasets:
                print(file)
            selected_dataset = input('\nSelect a dataset: ')
            print('Loading...')
        print('Dataset loaded\n')

    def preprocess_dataset(self):
        print('Preprocessing...')
        if not self.dataset.preprocess():
            print('\nNo dataset, load a dataset first\n')
            return
        print('Done\n')

    def print_text(self):
        dataset_texts = self.dataset.get_dataset()
        if not dataset_texts:
            print('\nNo dataset, load a dataset first\n')
            return
        dataset_length = len(dataset_texts)
        dataset_index = input(f'\n\nThere are {dataset_length} texts in the dataset.\n\nSelect an index (number): ')
        while True:
            try:
                if 0 <= int(dataset_index) < dataset_length:
                    print(f'\n{dataset_texts[int(dataset_index)]}\n')
                    return
            except:
                pass
            print('Not found')
            dataset_index = input(f'\n\nThere are {dataset_length} texts in the dataset.\n\nSelect an index (number): ')

    def create_term_document_matrix(self):
        print('Creating a matrix...')
        if not self.dataset.create_term_document_matrix():
            print('\nLoad and preprocess a dataset first\n')
            return
        print('Done\n')

    def print_matrix(self):
        if not self.dataset.print_matrix():
            print('\nCreate a term-document matrix first\n')
