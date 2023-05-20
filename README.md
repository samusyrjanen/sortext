# sortext

This is a text sorting app. The app takes one or multiple news articles as an input. Using the predetermined or user-given training data, it sorts those articles into similar groups.

## Documents

[Specification](docs/specification.md)  
[Week Report 1](docs/week_report_1.md)  

## Requirements

- Python 3.10 or newer
- Poetry

## Installation

- Clone the repository.
- Navigate to the cloned sortext directory, and install dependencies:  
`poetry install`

## Usage

You can list all available commands with:  
`poetry run invoke --list`  

To run a command:  
`poetry run invoke <command>`  

Commands:
- `test`
- `lint`

## Testing

Sortext uses pytest for unit testing, and pylint for linting.  
- Run the tests:  
`poetry run invoke test`  

- Run the linter:  
`poetry run invoke lint`

## Made By

Samu Syrjänen  
[License](LICENSE)
