![GHA workflow badge](https://github.com/samusyrjanen/sortext/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/samusyrjanen/sortext/branch/main/graph/badge.svg?token=TMTGIKOD27)](https://codecov.io/gh/samusyrjanen/sortext)  
[Coverage Report](https://app.codecov.io/gh/samusyrjanen/sortext/tree/main/src)

## Unit Tests

- Unit tests can be run with `poetry run invoke test`. It also creates a coverage report.

Unit tests are done with pytest. Test coverage is taken from files that contain the actual functionality of the app. All UI files are left outside of the test coverage. Additionally app.py and dataset.py are left outside of the test coverage, because app.py is simply used to import the necessary dependencies and launch the app, and dataset.py is used as a temporal storage of the handled data, and simply calls the actual functions.

The correct return values are hardcoded into the tests.

### dataset_reader.py

Dataset reader returns the available datasets and reads the dataset correctly.

The tests use the "archive.zip" dataset.

### text_preprocessor.py

Text preprocessor converts the data to lower case, removes punctuation and slash commands ("\n"), converts numbers into "num" strings, splits the data into single words, removes too short and too long words, and stemmes the words into their base form.

Hardcoded dataset used in tests:
- texts = ['To create a function in a class that outputs self.texts, you can define a method within the class that returns the value of the self.texts attribute.', 'n this example, the class MyClass has an __init__ method that initializes the self.texts attribute with a value passed as an argument. The get_texts method is defined to 100 times retrieve the value of self.texts and return it.', 'testing numbers: 123 1. 44, 45, and 46.']

### term_document_matrix.py

Returns a set of unique words from dataset, creates a term-document matrix of the preprocessed dataset, computes TF-IDF matrix, returns the most important terms in the dataset, and reduces the number of words on the dataset.

Because of the way the matrices are formed, they are not identical with each run. The indexing of columns varies because of the way the [unique words](https://github.com/samusyrjanen/sortext/blob/1f7287f7da9096dd0d2d0ae8a0da07b3bed41088/src/term_document_matrix.py#L19) are accumulated into a set. This makes testing a bit tricky. I have [tested](https://github.com/samusyrjanen/sortext/blob/1f7287f7da9096dd0d2d0ae8a0da07b3bed41088/src/tests/term_document_matrix_test.py#L17) the related functions, for example, by summing up terms, rows, or a whole matrix.

Hardcoded dataset used in tests:
- dataset = [['creat', 'function', 'class', 'output', 'selftext', 'defin', 'method', 'within', 'class', 'return', 'valu', 'selftext', 'attribut'], ['exampl', 'class', 'myclass', 'init', 'method', 'initi', 'selftext', 'attribut', 'valu', 'pass', 'argument', 'gettext', 'method', 'defin', 'num', 'time', 'retriev', 'valu', 'selftext', 'return'], ['test', 'number', 'num', 'num', 'num', 'num', 'num']]

## Running Time

The times have been measured using the "archive.zip" dataset which is located in "datasets" folder.

Name | Time |
-----|------|
Load a dataset | 0.1 s |
Preprocess a dataset | 9.4 s |
Create a term-document matrix | 1.0 s |
Create a TF-IDF matrix | 32.6 s |
Reduce the number of terms | 0.8 s |
Overall | 43.9 s |