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
        preprocessed = self.dataset.preprocess()
        if not preprocessed:
            print('\nNo dataset, load a dataset first\n')
            return
        print('Done\n')

    def print_text(self):
        dataset_texts = self.dataset.get_dataset()
        dataset_length = len(dataset_texts)
        if dataset_length == 0:
            print('\nNo dataset, load a dataset first\n')
            return
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
