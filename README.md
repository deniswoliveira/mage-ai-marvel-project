# Mage-AI Marvel Project
The Mage-AI Marvel Project is a data processing pipeline that uses Mage-AI to process character data from the Marvel API. \
The processed data is saved in an S3 bucket in Parquet format for further analysis and in a PostgreSQL database.

## Data Sources
The Mage-AI Marvel Project uses data from the Marvel API. \
Access keys can be created by following the Marvel tutorial: https://developer.marvel.com/documentation/getting_started

## Pipeline
The data pipeline consists of the following steps:

1.  Connect to the Marvel API using the access keys
2.  Retrieve character data from the API
3.  Process the data using Mage-AI
4.  Save the processed data in an S3 bucket and a PostgreSQL database

A flowchart of the pipeline is shown below:

<img src="https://github.com/deniswoliveira/mage-ai-marvel-project/blob/docs/images/architecture.jpeg" width=50% height=50%>

## Setup
To set up the project, follow these steps:

1.  Create an AWS account and create an S3 bucket \
2.  Create a user and update the read and write permissions on the bucket \
3.  Create access keys for the S3 bucket and the Marvel API \
4.  Clone the repository and navigate to the project directory \
5.  Copy the example files in the secrets and aws-variables.env directories and fill in the required information \
6.  Start the Docker containers using the command docker-compose up -d \

## Running the Pipeline
To run the pipeline, follow these steps:

1.  Access the Mage-AI web interface at http://localhost:6789/
2.  Click on the "marvel_api" pipeline
3.  Click on "Run pipeline now" and "Run now"
4.  Enter the trigger and check the pipeline result

## Contributing
If you would like to contribute to the project, please follow the guidelines in the CONTRIBUTING.md file. We welcome contributions from the community to improve the project and make it more useful for data analysts and Marvel fans.
