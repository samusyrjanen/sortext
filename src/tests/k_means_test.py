import unittest
from k_means import Kmeans
import numpy as np

class TestKmeans(unittest.TestCase):
    def setUp(self):
        self.matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
        self.k_means = Kmeans()
        
    def test_initialize_centroids(self):
        correct_coordinate_sum = 45
        correct_distances_sum = 41.56921938
        centroid_coordinates, distances = self.k_means.initialize_centroids(self.matrix, 3)
        coordinate_sum = np.sum(centroid_coordinates)
        distances_sum = np.sum(distances)
        rounded_distances_sum = "{:.8f}".format(distances_sum)
        self.assertEqual(coordinate_sum, correct_coordinate_sum)
        self.assertEqual(float(rounded_distances_sum), correct_distances_sum)
