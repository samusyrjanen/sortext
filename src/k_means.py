import random
import numpy as np

class Kmeans:
    '''
    Responsible for all k-means clustering functionality.

    Methods:
        initialize_centroids(matrix: np.ndarray, number_of_centroids: int): Creates initial centroids for each cluster.
    '''

    def initialize_centroids(self, matrix: np.ndarray, number_of_centroids: int):
        '''
        Initializes centroids for clusters.

        Args:
            matrix (np.ndarray): TF-IDF matrix.
            number_of_centroids (int): An integer indicating the desired number of clusters.

        Returns:
            centroid_coordinates (np.ndarray): An array of centroid coordinates. Rows are centroids, columns are terms.
            distances (np.ndarray): An array of distances between documents and centroids. Rows are centroids, columns are documents.
        '''

        matrix_shape = matrix.shape
        centroid_coordinates = np.zeros((number_of_centroids, matrix_shape[1]))#Rows are centroids, columns are terms
        distances = np.zeros((number_of_centroids, matrix_shape[0]))#Rows are centroids, columns are documents
        centroid_coordinates[0] = matrix[random.randint(0, matrix_shape[0]-1)]
        document_index = 0
        for document in matrix:
            distances[0, document_index] = self.euclidean_distance(centroid_coordinates[0], document)
            document_index += 1
        for centroid_index in range(1,number_of_centroids):
            farthest_document = np.argmax(np.amin(distances[:centroid_index], axis=0))
            centroid_coordinates[centroid_index] = matrix[farthest_document]
            document_index = 0
            for document in matrix:
                distances[centroid_index, document_index] = self.euclidean_distance(centroid_coordinates[centroid_index], document)
                document_index += 1
        return centroid_coordinates, distances

    def euclidean_distance(self, centroid: np.ndarray, document: np.ndarray):
        return np.sqrt(np.sum((centroid - document)**2))
