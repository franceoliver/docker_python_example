# Use an official Python 3.12 image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install pandas and any other necessary dependencies
# add anything else you need here.
RUN pip install pandas

# Optional: Install additional dependencies or copy your code
# COPY . /app

# Command to keep the container running (or you can remove this if you'll start a script)
CMD ["tail", "-f", "/dev/null"]
