# Data Engineering Assignment

This repository holds the Data Engineering Assignment. The assignment represents what a data engineer can be expected to do daily at Verusen: receiving raw data from different sources, transforming it into a structured format, and loading it into a database.

## Getting Started

1. To get started, fork the repository.
2. Then open up your terminal and clone the forked repository.

## The Assignment

The assignment is to create a **Python** script that reads the data from the CSV files, transforms it into a structured format, and loads it into a SQL (SQLLite, PSQL, MySQL, etc..) database.

### The Requirements

1. Idempotent: The script should be able to run multiple times without duplicating data in the database.
2. Script should run in Apache Spark using PySpark.

## The Data

The data directory contains data from [The Squirrel Census](https://www.thesquirrelcensus.com/). The `/data` is in CSV format and contains two files: `squirrel_census_2019.csv` and `squirrel_census_2020.csv`. The data is used to track the squirrel population in Central Park, New York City.

## The Deliverables

1. A Python script that reads the data from the CSV files, transforms it into a structured format, and loads it into a SQL database.
2. A `requirements.txt` file that contains all the dependencies needed to run the script.
3. A `README.md` file that explains how to run the script and any other information you think is important.
