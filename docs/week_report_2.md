### Tuesday 23.5.
- 4 h

I had some problems configuring a python version for github actions. It is working now. I added CI and test coverage badges to README. Created term_document_matrix.py for the TF-IDF stuff and tested it. At the moment it has a function for returning a set of all unique words in the dataset.

### Wednesday 24.5.
- 4 h

A term-document matrix can now be generated of a dataset.

### Friday 26.5.
- 6 h

Able to compute the normalized TF-IDF matrix from a loaded term-document matrix. I learned alot about numpy arrays and math operations related to them. Because of the way the matrices are formed, they are not identical each run. The indexing of columns varies because of the way the [unique words](https://github.com/samusyrjanen/sortext/blob/1f7287f7da9096dd0d2d0ae8a0da07b3bed41088/src/term_document_matrix.py#L19) are accumulated into a set. This makes testing a bit tricky. At the moment I have [tested](https://github.com/samusyrjanen/sortext/blob/1f7287f7da9096dd0d2d0ae8a0da07b3bed41088/src/tests/term_document_matrix_test.py#L17) the related functions, for example, by summing up rows or a whole matrix. I believe that is good enough.

### Working hours this week
14 h

Next week the term selection must be made to reduce the dimensions, and therefore the computing power required to run the k-means algorithm. Also the initializations of the clusters must be done before creating the actual k-means algorithm.
