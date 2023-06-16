class Interface:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        while True:
            command = input('========================= Commands =========================\n'
                            '(1) Input an article (optional)\n'
                            '(2) Run all commands\n'
                            '(3) Clear all inputs\n\n'
                            'Individual running commands:\n'
                            '(4) Load a dataset\n'
                            '(5) Preprocess the loaded dataset (takes around 10 seconds with archive.zip)\n'
                            '(6) Create a term-document matrix of the loaded dataset\n'
                            '(7) Convert term-document matrix into TF-IDF matrix (takes around 33 seconds with archive.zip)\n'
                            '(8) Reduce the number of terms to be used for clustering\n'
                            '(9) Initialize centroids (clusters)\n'
                            '(10) Run K-means clustering\n\n'
                            'Printing commands:\n'
                            '(11) Print a text from the loaded dataset\n'
                            '(12) Print a preprocessed text from the dataset\n'
                            '(13) Print matrix\n'
                            '(14) Print centroid coordinates\n'
                            '(15) Print clusters\n'
                            '(16) Print information of a specific document\n'
                            '(17) Print all documents belonging to a specific cluster\n\n'
                            '(0) Exit\n'
                            '============================================================\n\n'
                            'Select (number): ')
            if command == '1':
                self.commands.input_article()
            elif command == '2':
                self.commands.run_all()
            elif command == '3':
                self.commands.clear_inputs()
            elif command == '4':
                self.commands.read_dataset()
            elif command == '5':
                self.commands.preprocess_dataset()
            elif command == '6':
                self.commands.create_term_document_matrix()
            elif command == '7':
                self.commands.create_tfidf_matrix()
            elif command == '8':
                self.commands.reduce_terms()
            elif command == '9':
                self.commands.initialize_centroids()
            elif command == '10':
                self.commands.run_k_means()
            elif command == '11':
                self.commands.print_text()
            elif command == '12':
                self.commands.print_preprocessed_text()
            elif command == '13':
                self.commands.print_matrix()
            elif command == '14':
                self.commands.print_centroids()
            elif command == '15':
                self.commands.print_clusters()
            elif command == '16':
                self.commands.print_document_information()
            elif command == '17':
                self.commands.print_cluster()
            elif command == '18':
                self.commands.print_reduced_matrix()
            elif command == '0':
                print('Exit')
                return
            else:
                print('\nWrong command\n')
