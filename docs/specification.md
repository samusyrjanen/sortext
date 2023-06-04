# Specification

This is a text sorting app. The app takes one or multiple news articles as an input. Using the predetermined or user-given training data, it sorts those articles into similar groups.

## Languages

- English
- This is a Python app. Other programming language I know is JavaScript/TypeScript.

## Algorithms and Data Structures

The app uses TF-IDF, term-document matrices, LSI technique, and K-means clustering. Potential other algorithm to add is agglomerative clustering.  

I chose these algorithms because I am interested in natural language processing, and these algorithms are widely used. I had to select a slightly different topic as I had planned, because the original topic would have been overly hard and time consuming considering the amount of work that is planned for the course. The current topic could also be rather time consuming, since I have no previous experience with these algorithms.

## How Does It Work?

Here is a list of the needed functionalities:

- Get training data: The data can be anything, as long as it is text, and its guality is similar to the user input data. For example, I use news articles.
- Get user input.
- Preprocess the text data: This involves cleaning the text, removing punctuation, converting to lowercase, removing stop words, stemming the words reducing them to their base form, and performing any other necessary preprocessing steps.
- Convert the preprocessed text data into a term-document matrix: This matrix represents the frequency of each word in each document. Each row represents a document, and each column represents a word.
- Create a TF-IDF matrix: TF-IDF (Term Frequency-Inverse Document Frequency) is a technique that assigns weights to terms based on their importance in the corpus. The resulting matrix gives more weight to terms that are rare but important in a document.
- Apply normalization to the TF-IDF matrix to avoid the dominating effect of terms that are rare in other documents.
- Apply term reduction: Identifying the most important terms can be used to reduce the dimensionality of the matrix by truncating the less divisive terms. Because of the way TF-IDF matrix is formed, this can be done simply by summing up the values in each column.
- Choose the initial centroids for k-means using k-means++: First the number of centroids (seeds) must be selected. The k-means++ algorithm is then used to initialize the centroids for the k-means clustering. This step helps in selecting good initial cluster centers to improve the convergence of the algorithm. This step could be potentially replaced by agglomerative clustering, which could choose good starting centroids.
- Run the k-means algorithm: Apply the k-means algorithm to the matrix with the initial seeds obtained from k-means++. The algorithm assigns each document to one of the clusters based on their similarity, or euclidean distance in the multidimensional space (words being the dimensions). It iteratively updates the cluster centers and clusters documents until documents stop changing clusters.
- Obtain the final clusters: Once the k-means algorithm converges, the resulting clusters are considered final. Each document will be assigned to a specific cluster. The clusters can be represented by the documents assigned to each cluster. The clusters can be identified with the most relevant words.

## Time and Space Complexity

The time complexity of TF-IDF is O(nL log nL), where:
- n is total number of documents in a dataset
- L the average length of a document

Note that the result from TF-IDF can be saved for later use.

The space complexity of TF-IDF:
- Document-Term Matrix: The TF-IDF algorithm starts by constructing a Document-Term Matrix or a similar data structure that represents the frequency of each word in each document. The space required to store this matrix depends on the number of unique words and the number of documents. If there are N unique words and M documents, the space complexity of the matrix is O(N * M).
- Inverse Document Frequency: The IDF component of TF-IDF involves calculating the inverse document frequency for each word. This requires storing the IDF value for each word in a data structure. The space required for the IDF values depends on the number of unique words, so it is O(N).

The time complexity of k-means algorithm is O(n * k * d * i), where:
- n is number of documents
- k the number of clusters
- d the number of dimensions (words), which can be freely chosen
- i the number of iterations needed for convergence, which according to [Mining Text Data](https://helka.helsinki.fi/permalink/358UOH_INST/q5v72t/alma9933476355706253), is usually less than 5, given that the initial centroids are chosen well. (Hard cap can also be chosen)

If, despite all the efforts to minimize the app's running time it still takes too long, a solution could be to run the algorithm with the training data ahead of time. In that case, the app sould only need to compute the user input into TF-IDF values, and check from the preprocessed clusters which cluster it belongs to.

## Sources

- The book [Mining Text Data, by Aggarwal, Charu C. editor.; Zhai, ChengXiang. editor](https://helka.helsinki.fi/permalink/358UOH_INST/q5v72t/alma9933476355706253), has some good material regarding this topic.
- [k-means wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- [https://neptune.ai/blog/k-means-clustering](https://neptune.ai/blog/k-means-clustering)
- [An introduction to statistical learning : with applications in R, by James, Gareth (Gareth Michael), author.; Witten, Daniela, author.;Hastie, Trevor, author.;Tibshirani, Robert, author.](https://helka.helsinki.fi/permalink/358UOH_INST/1rnip4l/alma9934192676106253)
- [https://www.cs.helsinki.fi/group/dime/lado/k06/exerc/ex1.html](https://www.cs.helsinki.fi/group/dime/lado/k06/exerc/ex1.html)
- [TF-IDF time complexity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4958984/)
- [Training Data](https://www.kaggle.com/datasets/shivamkushwaha/bbc-full-text-document-classification)

## Curriculum

tietojenkäsittelytieteen kandidaatti (TKT)
