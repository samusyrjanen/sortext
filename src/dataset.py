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
    '''

    def __init__(self, dataset_reader, text_preprocessor):
        self.dataset = []
        self.dataset_reader = dataset_reader
        self.text_preprocessor = text_preprocessor

    def get_dataset_files(self):
        return self.dataset_reader.get_dataset_files()

    def read_dataset(self, file_name):
        self.dataset = self.dataset_reader.read_dataset(file_name)
        if not self.dataset:
            self.dataset = []
            return False
        return True

    def preprocess(self):
        if self.dataset == []:
            return False
        self.dataset = self.text_preprocessor.preprocess(self.dataset)
        return True

    def get_dataset(self):
        return self.dataset
