### Tuesday & Wednesday 30.-31.5.
- 10 h

I have been researching the best ways to reduce the number of terms in the TF-IDF matrix. Previously I had planned to use latent semantic indexing (LSI), which is based on the singular value decomposition (SVD). At the moment, I have decided to simply sum up the values of each column in the matrix to calculate the importance of the term. Because of the way TF-IDF is calculated, this should serve as a good indicator for which terms to retain. If I have time, I can return to this solution later, and apply LSI or some other method to compare the results.

### Thursday 1.6.
- 3 h

Created a testing document and some running time measurements into the code.

### Saturday 3.6.
- 6 h

Centroids can now be initialized using K-means++.

### Sunday 4.6.
- 5 h

The functionality for K-means algorithm is finished. Learned more numpy array handling.

### Working hours this week
24 h

Next I need to enhance the user interface and add functionalities for adding own texts for clustering. There also needs to be a better way to inspect the different documents and clusters.
