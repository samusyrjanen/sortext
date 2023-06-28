# sortext

![GHA workflow badge](https://github.com/samusyrjanen/sortext/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/samusyrjanen/sortext/branch/main/graph/badge.svg?token=TMTGIKOD27)](https://codecov.io/gh/samusyrjanen/sortext)

This is a text sorting app. The app uses a dataset of old bbc news articles, and takes additional news articles as an input. The news articles are converted into a matrix, which indicates the importance of each word in an article, and it sorts those articles into similar groups using k-means clustering algorithm. The resulting clusters contain similar texts, and they can be browsed.

## Documents

[Instructions](docs/instructions.md)  
[Specification](docs/specification.md)  
[Testing Document](docs/testing_document.md)  
[Implementation Document](docs/implementation_document.md)  

[Week Report 1](docs/week_report_1.md)  
[Week Report 2](docs/week_report_2.md)  
[Week Report 3](docs/week_report_3.md)  
[Week Report 4](docs/week_report_4.md)  
[Week Report 5](docs/week_report_5.md)  
[Week Report 6](docs/week_report_6.md)  

## Requirements

- Python 3.10 or newer
- Poetry

## Installation

- Clone the repository.
- Navigate to the cloned sortext directory, and install dependencies:  
`poetry install`

## Usage

### Start  
`poetry run invoke start`  

### Commands

If you run `poetry shell`, the "poetry run" part will not be needed in the commands. Exit poetry shell with `exit`.

You can list all available commands with:  
`poetry run invoke --list`  

To run a command:  
`poetry run invoke <command>`  

Commands:
- `start`
- `test`
- `lint`

## Testing

Sortext uses pytest for unit testing, and pylint for linting.  
- Run the tests:  
`poetry run invoke test`  

- Run the linter:  
`poetry run invoke lint`

## Training Data

[https://www.kaggle.com/datasets/shivamkushwaha/bbc-full-text-document-classification](https://www.kaggle.com/datasets/shivamkushwaha/bbc-full-text-document-classification)

This app uses BBC news articles as training data. The dataset consists of 2225 documents corresponding to stories in five topical areas (business, entertainment, politics, sport, tech) from 2004-2005.  

Publication:  
D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006.  

All rights, including copyright, in the content of the original articles are owned by the BBC.  
[License](https://opendatacommons.org/licenses/dbcl/1-0/)

## Made By

Samu Syrjänen  
[License](LICENSE)
