# Instructions

## Requirements

- Python 3.10 or newer
- Poetry

## Installation

- Clone the repository.
- Navigate to the cloned sortext directory, and install dependencies:  
`poetry install`

## Running Instructions

### Start  
`poetry run invoke start`  

### Poetry Commands

If you run `poetry shell`, the "poetry run" part will not be needed in the commands. Exit poetry shell with `exit`.

You can list all available commands with:  
`poetry run invoke --list`  

To run a command:  
`poetry run invoke <command>`  

Commands:
- `start`
- `test`
- `lint`

## Usage

After starting, the program will list all user commands:  
```
========================= Commands =========================
(1) Input an article (optional)  
(2) Run all commands  
(3) Clear all inputs  

Individual running commands:  
(4) Load a dataset  
(5) Preprocess the loaded dataset (takes around 10 seconds with archive.zip)  
(6) Create a term-document matrix of the loaded dataset  
(7) Convert term-document matrix into TF-IDF matrix (takes around 33 seconds with archive.zip)  
(8) Reduce the number of terms to be used for clustering  
(9) Initialize centroids (clusters)  
(10) Run K-means clustering  

Printing commands:  
(11) Print a text from the loaded dataset  
(12) Print a preprocessed text from the dataset  
(13) Print matrix  
(14) Print centroid coordinates  
(15) Print clusters  
(16) Print information of a specific document  
(17) Print all documents belonging to a specific cluster  

(0) Exit  
============================================================
```

The commands are selected by typing the corresponding number, for example `2`  

- Command 2 runs all the operations.
- Commands 1 and 3 are used to input own texts into the algorithm.
- Commands 4-10 are all included in command 2, but are also included individually for more flexible usage.
- Commands 11-17 are printing commands, which can be used to view the results.
