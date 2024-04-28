# Data Engineering Assignment Solution

This repository is my solution for the Data Engineering Assignment. Here are some of the decisions I took to solve the assigment:

- Use a SQLite to store the data, for simplicity's sake
- Use poetry for dependency management.
- Add an extra table `OtherAnimalSightings` to be able to count animal types by park. I ended up not using this because query number 3 did not ask to count by animal type.

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Setup](#setup)
- [Running the Code Locally](#running-the-code-locally)
- [Running the Code in Docker](#running-the-code-in-docker)

## Pre-requisites

- Python 3.7 or higher.
- Apache Spark (for local run).
- Poetry for managing Python dependencies.
- Docker.

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/squirrel-census.git
    cd squirrel-census
    ```


## Running the Code Locally
1. **Install Python dependencies**:

    Ensure you have Poetry installed and then install the dependencies:

    ```bash
    poetry install --no-root
    ```

2. **Run the script**:

    ```bash
    poetry run python main.py
    ```

## Running the Code in Docker

1. **Build the Docker container**:

    In the root directory of the project (where the `Dockerfile` is located), build the Docker container:

    ```bash
    docker build -t spark-squirrel-census .
    ```

2. **Run the Docker container**:

    Run the Docker container:

    ```bash
    docker run --rm spark-squirrel-census
    ```
    
    To store the squirrel_census.db locally, mount the current working directory:

    ```bash
    docker run --rm -v $(pwd):/app spark-squirrel-census
    ```