class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('Commands:\n'
                            '(1) Load a dataset\n'
                            '(2) Preprocess the loaded dataset (takes around 13 seconds with archive.zip)\n'
                            '(3) Create a term-document matrix of the loaded dataset\n'
                            '(4) Convert term-document matrix into TF-IDF matrix (takes around 40 seconds with archive.zip)\n'
                            '(5) Reduce the number of terms to be used for clustering\n'
                            '(6) Initialize centroids (clusters)\n'
                            '(7) Run K-means clustering\n'
                            '(8) Print a text from the loaded dataset\n'
                            '(9) Print the matrix\n'
                            '(10) Print the reduced matrix\n'
                            '(11) Print centroid coordinates\n'
                            '(12) Print clusters\n'
                            '(13) Run all\n'
                            '(0) Exit\n\n'
                            'Select (number): ')
            if command == '1':
                self.commands.read_dataset()
            elif command == '2':
                self.commands.preprocess_dataset()
            elif command == '3':
                self.commands.create_term_document_matrix()
            elif command == '4':
                self.commands.create_tfidf_matrix()
            elif command == '5':
                self.commands.reduce_terms()
            elif command == '6':
                self.commands.initialize_centroids()
            elif command == '7':
                self.commands.run_k_means()
            elif command == '8':
                self.commands.print_text()
            elif command == '9':
                self.commands.print_matrix()
            elif command == '10':
                self.commands.print_reduced_matrix()
            elif command == '11':
                self.commands.print_centroids()
            elif command == '12':
                self.commands.print_clusters()
            elif command == '13':
                self.commands.run_all()
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
