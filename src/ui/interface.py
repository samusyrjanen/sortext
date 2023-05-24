class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('Commands:\n'
                            '(1) Load a dataset\n'
                            '(2) Preprocess the loaded dataset (takes usually couple of seconds)\n'
                            '(3) Print a text from the loaded dataset\n'
                            '(4) Create a term-document matrix of the loaded dataset\n'
                            '(5) Print the term-document matrix\n'
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
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
