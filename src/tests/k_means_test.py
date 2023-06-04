import unittest
from k_means import Kmeans
import numpy as np

class TestKmeans(unittest.TestCase):
    def setUp(self):
        self.matrix = np.array([[1,2,3,5,6], [4,5,6,6,5], [7,8,1,2,9], [6,6,6,7,8], [2,1,2,2,1]])
        self.centroids = np.array([[3,3,3,3,3], [5,5,5,5,5], [1,1,1,1,1]])
        self.k_means = Kmeans()
        
    def test_initialize_centroids(self):
        centroid_coordinates, distances = self.k_means.initialize_centroids(self.matrix, 3)
        number_of_zeros = np.sum(distances == 0)
        self.assertEqual(centroid_coordinates.any(), self.matrix.any())
        self.assertEqual(number_of_zeros, 3)

    def test_euclidean_distance(self):
        correct = 5.385164807134504
        distance = self.k_means.euclidean_distance(self.matrix[0], self.matrix[1])
        self.assertEqual(distance, correct)

    def test_get_clusters(self):
        correct = np.array([0, 4, 2, 2, 4])
        clusters = self.k_means.get_clusters(self.matrix)
        self.assertEqual(clusters.all(), correct.all())

    def test_calculate_distances(self):
        correct = np.array([[4.24264069,5.19615242,9.05538514,8.24621125,3.31662479],
                            [5.47722558,1.73205081,7.34846923,4.,7.68114575],
                            [6.78232998,9.53939201,12.24744871,12.64911064,1.73205081]])
        distances = np.zeros((3,5))
        distances = self.k_means.calculate_distances(self.matrix, distances, self.centroids)
        self.assertEqual(distances.all(), correct.all())

    def test_calculate_new_centroid_coordinates(self):
        correct = np.array([[1, 2, 3, 5, 6], [5, 6, 4, 5, 7], [2, 1, 2, 2, 1]])
        distances = np.zeros((3,5))
        distances = self.k_means.calculate_distances(self.matrix, distances, self.centroids)
        clusters = self.k_means.get_clusters(distances)
        centroid_coordinates = self.k_means.calculate_new_centroid_coordinates(self.matrix, clusters, self.centroids)
        self.assertEqual(centroid_coordinates.all(), correct.all())

    def test_run_k_means(self):
        correct_centroid_coordinates = np.array([[1, 2, 3, 5, 6], [5, 6, 4, 5, 7], [2, 1, 2, 2, 1]])
        correct_clusters = np.array([0, 1, 1, 1, 2])
        distances = np.zeros((3,5))
        distances = self.k_means.calculate_distances(self.matrix, distances, self.centroids)
        centroid_coordinates, clusters = self.k_means.run_k_means(self.matrix, self.centroids, distances, 3)
        self.assertEqual(centroid_coordinates.all(), correct_centroid_coordinates.all())
        self.assertEqual(clusters.all(), correct_clusters.all())
