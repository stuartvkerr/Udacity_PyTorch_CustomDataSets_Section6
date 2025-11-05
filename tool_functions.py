from parameters import *
from imports import Path, requests, zipfile

def get_images():
    # Setup path to data
    data_path = Path(FOLDER_NAME)
    image_path = data_path / "pizza_sushi_steak"

    # If the image path does not exist, download it and process
    if image_path.is_dir():
        print(f"{image_path} directory exists, skipping download...")
    else:
        print(f"{image_path} does not exist, downloading...")
        image_path.mkdir(parents=True, exist_ok=True)

    with open(data_path / "pizza_sushi_steak.zip", "wb") as f:
        request = requests.get(RAW_IMAGE_SOURCE)
        print("Downloading images...")
        f.write(request.content)
        print("Download complete...")
        # Unzip the loaded file
        print("Unzipping image zip file")
        with zipfile.ZipFile(data_path / "pizza_sushi_steak.zip", "r") as zip_ref:
            zip_ref.extractall(image_path)
            print("Unzip complete...")
            print(f"Images contained in {image_path}")




