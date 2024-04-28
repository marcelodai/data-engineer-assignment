FROM bitnami/spark:latest

USER root
RUN apt-get update && apt-get install -y curl python3-pip && \
    pip3 install poetry

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock into the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the source code into the container
COPY . /app

# Run main.py when the container launches
CMD ["poetry", "run", "python", "main.py"]