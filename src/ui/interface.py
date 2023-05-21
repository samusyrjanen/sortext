class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('Commands:\n(1) Load a dataset\n(2) Preprocess a dataset (takes usually couple of seconds)\n(3) Print a text from dataset\n(0) Exit\n\nSelect (number): ')
            if command == '1':
                self.commands.read_dataset()
            elif command == '2':
                self.commands.preprocess_dataset()
            elif command == '3':
                self.commands.print_text()
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
