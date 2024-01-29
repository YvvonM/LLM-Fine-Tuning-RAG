# Use an official PyTorch image as a parent image
#FROM pytorch/pytorch:latest

# Use an official Python or PyTorch image as a parent image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into the container
COPY . .

# Define the command to run your application
CMD [ "python", "fine_tune_script.py" ]