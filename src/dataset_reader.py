import zipfile
import os

class DatasetReader:
    '''
    DatasetReader is used to select, and read a dataset into a list.

    Methods:
        get_database_files(): Returns a list of files in "datasets" directory.
        read_dataset(file: str): Reads and returns the selected dataset.
        input_article(): Creates a .txt file of a user input.
        clear_inputs(): Deletes all user inputs.
        read_user_input(): Reads and returns the user input texts.
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

    def input_article(self, text: str):
        directory = os.listdir('user_input')
        filename = f'input{len(directory)+1}.txt'
        with open('user_input/'+filename, 'w', encoding='utf-8') as file:
            file.write(text)

    def clear_inputs(self):
        for filename in os.listdir('user_input'):
            if filename.endswith('.txt'):
                file_path = os.path.join('user_input', filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    def read_user_input(self):
        texts = []
        file_names = os.listdir('user_input')
        file_names = sorted(file_names)
        for filename in file_names:
            if filename.endswith('.txt'):
                file_path = os.path.join('user_input', filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as txt_file:
                        text = txt_file.read()
                        texts.append(text)
                except UnicodeDecodeError:
                    print(f'Skipping file: {filename} - contains non-UTF-8 characters')
        return texts
