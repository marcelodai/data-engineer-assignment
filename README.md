# Data Engineering Assignment

This repository holds the Data Engineering Assignment. The assignment represents what a data engineer can be expected to do daily at Verusen: receiving raw data from different sources, transforming it into a structured format, and loading it into a database.

The assignment is to create a **Python** script(s) that reads the data from the CSV files, transforms it into a structured format per the deliverable requirements, and loads it into a SQL (SQLLite, PSQL, MySQL, etc..) database.

## The Data

The data directory contains data from [The Squirrel Census](https://www.thesquirrelcensus.com/). The data is in CSV format and contains two files: `/data/park-data.csv` and `/data/squirrel-data.csv`. The data is used to track the squirrel population in Central Park, New York City.

## The Assignment

### The Requirements

1. Idempotent: The script should be able to run multiple times without duplicating data in the database.
2. Script should run in Apache Spark (Docker container) using PySpark.

### The Deliverables

Your task is to **normalize the data** as much as possible for querying purposes. The queries and questions we are trying to optimize for are:

1. How many squirrels are there in each Park?
2. How many squirrels are there in each Borough?
3. A count of "Other Animal Sightings" by Park.
4. What is the most common activity for Squirrels? (e.g. eating, running, etc..)
5. A count of all Primary Fur Colors by Park.

### Output

1. The final output should be your python code that performs the ETL process, your final database schema populated, and the queries to answer the questions above.
2. Code and script should be runnable in a Docker container with Apache Spark.

### The Submission

Your submission will rest in your repository. The final product should be accompanied with a README.md file that explains how to run the script, and any other relevant information.

We will talk through it as a team during the interview process.

Key areas of interest include:

- Code Structure: How well is your code organized? How clear is the logic?
- Data Transformation: How well did you normalize the data?
- Database Schema: How well did you design the database schema?
- Development Env: How easy is it to get your code up and running?
- Communication: How well did you document your code and how well can you explain your decisions?
