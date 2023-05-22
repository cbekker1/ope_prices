# OPE Retail Price Loader

This project uses the platform [Open Price Engine](https://www.openpricengine.com/) to extract, transform, and load data into a CSV file located in the data folder. In addition, it lets the user create a line graph using the loaded data. 

## Simplified process diagram

                  +--------------+
                  |    OPE (API) |
                  +--------------+
                         |
                         |
                         v
                  +--------------+
                  |     ETL	   |
                  +--------------+
                         |
                         |
                         v
                  +--------------+
                  |   	CSVs     |
                  +--------------+
                         |
                         |
                         v
                  +--------------+
                  |   Visual     |
                  |(Line Chart)  |
                  +--------------+


## Usage

To extract data csv's, open the "data_load.py" file, pass in the parameters start date, end date and desired product type and run it. The resulting CSV files will be located in the data folder. To visualise the extracted data, open data_visualisation.py and run the script to produce line plots with the extracted data.

## Configuration of environment

On your pc, create an environment variable named 'MY_REPO_HOME' with the folder path of where the git repo is cloned to.
This sets the working directory to the folder that contains the cloned repository.

## Requirements

- Python 3.x
- Requests library
- Pandas library
- Os library
- Matplotlib library
- Requests library
- Pandas library
- Json library
- Seaborn library

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.