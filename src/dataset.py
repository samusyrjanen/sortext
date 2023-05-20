import zipfile
import os

class Dataset:
    '''
    Dataset() is used to select, and read a dataset into a list.

    Methods:
        read_dataset(file: str)
        get_texts() returns the texts (a list of strings, each string being a text document).
    '''

    def __init__(self):
        self.texts = []

    def read_dataset(self, file: str):
        '''
        Reads the dataset. The file must be in "datasets" folder, and the text documents must be in .txt files.
        One text document per .txt file.
        
        Args:
            file (str): A zip file to be read. example: 'archive.zip'
        '''

        with zipfile.ZipFile(os.path.join('datasets', file), 'r') as dataset:
            for file_info in dataset.infolist():
                if file_info.filename.endswith('.txt'):
                    with dataset.open(file_info) as txt_file:
                        try:
                            text = txt_file.read().decode('utf-8')
                            self.texts.append(text)
                        except UnicodeDecodeError:
                            print(f'Skipping file: {file_info.filename} - contains non-UTF-8 characters')

    def get_texts(self):
        return self.texts
