# OPE Retail Price Loader

This project uses the platform [Open Price Engine](https://www.openpricengine.com/) to extract, transform, and load data into a CSV file located in the data folder.

## Usage

To execute this process, open the "data_load.py" file, pass in the start date, end date and desired product type and run it. The resulting CSV file will be located in the data folder.
On your pc, create an environment variable named 'MY_REPO_HOME' with the folder path of where the git repo is cloned to.
This sets the working directory to the folder that contains the cloned repository.

## Requirements

- Python 3.x
- Requests library
- Pandas library

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.