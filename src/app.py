from dataset_reader import DatasetReader
from dataset import Dataset
from text_preprocessor import TextPreprocessor
from term_document_matrix import TermDocumentMatrix
from k_means import Kmeans
from ui.interface import Interface
from ui.commands import Commands

def main():
    '''
    Starts the app.
    '''

    dataset_reader = DatasetReader()
    text_preprocessor = TextPreprocessor()
    term_document_matrix = TermDocumentMatrix()
    k_means = Kmeans()
    dataset = Dataset(dataset_reader, text_preprocessor, term_document_matrix, k_means)
    commands = Commands(dataset)
    interface = Interface(commands)
    print('\nsortext\n')
    interface.start()


if __name__ == "__main__":
    main()
