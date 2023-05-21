from dataset_reader import DatasetReader
from dataset import Dataset
from text_preprocessor import TextPreprocessor
from ui.interface import Interface
from ui.commands import Commands

def main():
    '''
    Starts the app.
    '''

    dataset_reader = DatasetReader()
    text_preprocessor = TextPreprocessor()
    dataset = Dataset(dataset_reader, text_preprocessor)
    commands = Commands(dataset)
    interface = Interface(commands)
    print('\nsortext\n')
    interface.start()


if __name__ == "__main__":
    main()
