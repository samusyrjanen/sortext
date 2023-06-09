## The first days

### Sunday 7.5.
- 5 h

### Saturday 13.5.
- 3 h

I began planning my topic a week before the official course start. I wanted to make an app that could analyze text based content at least somewhat intelligently. First, I explored the idea of making the app categorize a news article into negative, neutral, or positive category based on its sentiment. For this task I would have used a support vector machine (SVM) algorithm. However, SVM turned out to be more complex than I anticipated, and I decided to think of a slightly new topic.

## This week

### Monday 15.5.
- 5 h

### Tuesday 16.5.
- 7 h

At the start of this week, I began exploring the possibility to use an easier, k-means clustering algorithm to categorize the news articles. Although this method is unable to categorize articles into predetermined categories, it was easier to implement than SVM, and it uses unsupervised learning instead of supervised learning, making it easier to find desired training data. For this algorithm, the text data would need to be processed into a k-means-friendly form. This meant yet more planning and reading.

### Wednesday 17.5.
- 9 h

After couple days of research, I felt confident enough that I could learn the necessary skills to carry out my planned topic. In wednesday afternoon I wrote the specifications about the project, and joined the course's Labtool page. At this point, the [specification.md](specification.md) is a good summary of my learning.

### Thursday 18.5.
- 3 h

In thursday morning I began writing this document, reflecting what I had done in the passed days. At this point almost everything is ready to start the actual creation of the app. The first thing I will start by is creating a good environment for the codebase and plan the structure and order, by which I will start the development.

### Friday 19.5.
- 5 h

I created a text preprocessing file, which I will be running before TF-IDF. The preprocessing modifies text in the following way: all letters are lower case, remove punctuation, numbers are turned into 'num'-strings, remove words with less than 3 or more than 20 characters, words are stemmed into their base form. Tests are also done, and the requirements, installation, and testing are documented in [README](../README.md).

### Saturday 20.5.
- 6 h

Today I started by creating invoke tasks for the commonly used commands. I also added linting and coverage report for the tests, and documented them. Created dataset.py that reads the dataset into a list, and added tests for it. I found a good dataset of over 2000 BBC articles, and added it to datasets folder. The copyright and license can be found in [README](../README.md). The user can also add their own datasets into "datasets" folder. The functionality for selecting a dataset will be made later.

### Sunday 21.5.
- 5 h

I began the day by creating a command line interface. I made a new dataset.py file which is responsible for handling the data by comminucating with dataset_reader.py and text_preprocessor.py. The new app.py is used to launch the app. Made tests, documentations, and an invoke command for launching the app. I haven't stumbled into any problems yet, and have no questions at the moment.

### Working hours this week
48 h  

I will probably slow down the work pace since the hours seem to sum up quickly.

## Next week

Next week I will probably be creating the term-document matrix and TF-IDF stuff.