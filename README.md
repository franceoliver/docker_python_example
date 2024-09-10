# Python 3.12 + Pandas Docker Environment

This guide explains how to build and run a Docker container with Python 3.12 and Pandas installed, and how to execute your Python scripts using this container.

## Prerequisites

- Docker installed on your machine
- A `Dockerfile` with Python 3.12 and Pandas setup

## Steps

### 1. Build the Docker Image

To build the Docker image, run the following command in the directory where your `Dockerfile` is located:

```bash
 docker build -t python3.12-pandas .
```

This command creates an image named `python3.12-pandas`.

### 2. Run the Docker Container

After building the image, run the container with the following command:

```bash
 docker run -d --name python3.12-container -v $(pwd):/app python3.12-pandas
```

- `-d` runs the container in detached mode (in the background).
- `--name` specifies the name of the container (`python3.12-container`).
- `-v $(pwd):/app` mounts your current directory to `/app` inside the container, so any files in your local directory can be accessed inside the container.

### 3. Verify the Container is Running

You can check if the container is running using the following command:

```bash
docker ps
```

Look for `python3.12-container` in the list of running containers.

### 4. List Installed Python Packages

To view all Python packages installed inside the Docker container, use the following command:

```bash
 docker exec -it python3.12-container pip list 
```

This will display a list of installed Python packages, including `pandas` Use this to confirm the correct packages are being installed.

### 5. Run Python Scripts Inside the Container

To execute your Python script inside the Docker container, use the `docker exec` command. Replace `your_script.py` with the path to your script:

```bash
 docker exec -it python3.12-container python /app/dummy_pandas_script.py
```

This will run your Python script within the container's environment using Python 3.12 and Pandas.

### 6. Stop and Remove the Docker Container

When you're done with the container, you can stop and remove it using the following commands:

Stop the container:

```bash
 docker stop python3.12-container 
```

Remove the container:

```bash
 docker rm python3.12-container 
```