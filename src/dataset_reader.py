import zipfile
import os

class DatasetReader:
    '''
    DatasetReader is used to select, and read a dataset into a list.

    Methods:
        get_database_files(): Returns a list of files in "datasets" directory.
        read_dataset(file: str): Reads and returns the selected dataset.
    '''

    def get_dataset_files(self):
        files = []
        directory = os.listdir('datasets')
        for file in directory:
            if os.path.isfile(os.path.join('datasets', file)):
                files.append(file)
        return files

    def read_dataset(self, file: str):
        '''
        Reads a dataset. The file must be in "datasets" folder, and the text documents must be in .txt files.
        One text document per .txt file.
        
        Args:
            file (str): A zip file to be read. example: 'archive.zip'

        Returns:
            texts: A list of text documents.
            False: If file is not found in datasets.
        '''

        datasets = self.get_dataset_files()
        if file not in datasets:
            return False

        texts = []
        with zipfile.ZipFile(os.path.join('datasets', file), 'r') as dataset:
            for file_info in dataset.infolist():
                if file_info.filename.endswith('.txt'):
                    with dataset.open(file_info) as txt_file:
                        try:
                            text = txt_file.read().decode('utf-8')
                            texts.append(text)
                        except UnicodeDecodeError:
                            print(f'Skipping file: {file_info.filename} - contains non-UTF-8 characters')
        return texts
