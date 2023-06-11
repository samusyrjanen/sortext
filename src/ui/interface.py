class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('========================= Commands =========================\n'
                            '(1) Run all\n\n'
                            '(2) Load a dataset\n'
                            '(3) Preprocess the loaded dataset (takes around 10 seconds with archive.zip)\n'
                            '(4) Create a term-document matrix of the loaded dataset\n'
                            '(5) Convert term-document matrix into TF-IDF matrix (takes around 33 seconds with archive.zip)\n'
                            '(6) Reduce the number of terms to be used for clustering\n'
                            '(7) Initialize centroids (clusters)\n'
                            '(8) Run K-means clustering\n\n'
                            'Print commands:\n'
                            '(9) Print a text from the loaded dataset\n'
                            '(10) Print a preprocessed text from the dataset\n'
                            '(11) Print matrix\n'
                            '(12) Print centroid coordinates\n'
                            '(13) Print clusters\n'
                            '(14) Print information of a specific document\n'
                            '(15) Print all documents belonging to a specific cluster\n\n'
                            '(0) Exit\n'
                            '============================================================\n\n'
                            'Select (number): ')
            if command == '1':
                self.commands.run_all()
            elif command == '2':
                self.commands.read_dataset()
            elif command == '3':
                self.commands.preprocess_dataset()
            elif command == '4':
                self.commands.create_term_document_matrix()
            elif command == '5':
                self.commands.create_tfidf_matrix()
            elif command == '6':
                self.commands.reduce_terms()
            elif command == '7':
                self.commands.initialize_centroids()
            elif command == '8':
                self.commands.run_k_means()
            elif command == '9':
                self.commands.print_text()
            elif command == '10':
                self.commands.print_preprocessed_text()
            elif command == '11':
                self.commands.print_matrix()
            elif command == '12':
                self.commands.print_centroids()
            elif command == '13':
                self.commands.print_clusters()
            elif command == '14':
                self.commands.print_document_information()
            elif command == '15':
                self.commands.print_cluster()
            elif command == '16':
                self.commands.print_reduced_matrix()
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
