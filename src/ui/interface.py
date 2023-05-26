class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('Commands:\n'
                            '(1) Load a dataset\n'
                            '(2) Preprocess the loaded dataset (takes around 13 seconds with archive.zip)\n'
                            '(3) Print a text from the loaded dataset\n'
                            '(4) Create a term-document matrix of the loaded dataset\n'
                            '(5) Print the matrix\n'
                            '(6) Convert term-document matrix into TF-IDF matrix (takes around 40 seconds with archive.zip)\n'
                            '(7) run all\n'
                            '(0) Exit\n\n'
                            'Select (number): ')
            if command == '1':
                self.commands.read_dataset()
            elif command == '2':
                self.commands.preprocess_dataset()
            elif command == '3':
                self.commands.print_text()
            elif command == '4':
                self.commands.create_term_document_matrix()
            elif command == '5':
                self.commands.print_matrix()
            elif command == '6':
                self.commands.create_tfidf_matrix()
            elif command == '7':
                self.commands.run_all()
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
