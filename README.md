# Mage-AI Marvel Project

## Project's goal
The Mage-AI Marvel Project aims to use the Mage-AI tool to create a data pipeline to process characters data from the Marvel API, and save the new dataset in an s3 bucket in parquet format for further analysis and in a PostgreSQL database.

<img src="https://github.com/deniswoliveira/mage-ai-marvel-project/blob/docs/images/architecture.jpeg" width=50% height=50%>

## Setup

- Creating access keys for Marvel API
	-	Follow the marvel tutorial for creating access keys https://developer.marvel.com/documentation/getting_started.

- Create an s3 bucket
	- Create an AWS account https://docs.aws.amazon.com/accounts/latest/reference/welcome-first-time-user.html.
	- Create a bucket in s3 https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html.
	- Create a user https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html.
	- Update the read and write permissions on the bucket https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html.
	- Create the access key and secret key https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html.

- Setting the environment variables
	Remove the .example suffix in the files below and fill in the information as requested in each file.
	- secrets/marvel_credentials.json.example
	- secrets/s3_marvel_api_conf.json.example
	- aws-variables.env.example
	
-	Starting the docker containers
	-	Install docker and docker-compose https://docs.docker.com/get-docker/.
	-	run the command: \
		 To Start ```docker-compose up -d``` \
		 To Stop ```docker-compose stop```

-	Running the pipeline on mage
	-	Enter the url http://localhost:6789/ \
		<img src="https://github.com/deniswoliveira/mage-ai-marvel-project/blob/docs/images/home.png" width=75% height=75%>
	-	Click in **"marvel_api"** pipeline
	- Click in **"Run pipeline now"** and **"Run now"**
	- Enter the trigger and check the pipeline result
