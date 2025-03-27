import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Make sure the data directory exists
os.makedirs("data", exist_ok=True)

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Dataset identifier from the URL
dataset = "shariful07/student-mental-health"

# Download dataset to 'data' folder
api.dataset_download_files(dataset, path="data", unzip=True)

print("Download complete.")
