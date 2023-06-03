### Tuesday & Wednesday 30.-31.5.
- 10 h

I have been researching the best ways to reduce the number of terms in the TF-IDF matrix. Previously I had planned to use latent semantic indexing (LSI), which is based on the singular value decomposition (SVD). At the moment, I have decided to simply sum up the values of each column in the matrix to calculate the importance of the term. Because of the way TF-IDF is calculated, this should serve as a good indicator for which terms to retain. If I have time, I can return to this solution later, and apply LSI or some other method to compare the results.

### Thursday 1.6.
- 3 h

Created a testing document and some running time measurements into the code.

### Saturday 3.5.
- 6 h

Centroids can now be initialized using k-means++.
