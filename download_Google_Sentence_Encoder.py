import os
import gdown
from zipfile import ZipFile

def download_and_extract_model():
    # Define paths
    base_dir = 'server'
    model_dir = os.path.join(base_dir, 'pre_trained_models')
    file_path = os.path.join(model_dir, 'model.zip')
    
    # Ensure model directory exists
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Define Google Drive file id
    # Extract file id from the Google Drive link (it's the string between 'd/' and '/view')
    file_id = '1628XBJrFBaRIA4Tizx2JWuL_R0VSgtxn'
    url = f'https://drive.google.com/uc?id={file_id}'

    # Download file from Google Drive
    gdown.download(url, file_path, quiet=False)

    # Extract the downloaded zip file
    with ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(model_dir)

    # Clean up zip file
    if os.path.exists(file_path):
        os.remove(file_path)

download_and_extract_model()

