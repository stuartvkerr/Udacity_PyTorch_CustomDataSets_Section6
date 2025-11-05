from parameters import *
from imports import torch, Path, requests, zipfile, v2

## Load raw images if not already present
def get_images():
    # If the image path does not exist, download it and process
    if IMAGE_PATH.is_dir():
        print(f"{IMAGE_PATH} directory exists, skipping download...")
    else:
        print(f"{IMAGE_PATH} does not exist, downloading...")
        IMAGE_PATH.mkdir(parents=True, exist_ok=True)

    with open(DATA_PATH / "pizza_sushi_steak.zip", "wb") as f:
        request = requests.get(RAW_IMAGE_SOURCE)
        print("Downloading images...")
        f.write(request.content)
        print("Download complete...")
        # Unzip the loaded file
        print("Unzipping image zip file")
        with zipfile.ZipFile(DATA_PATH / "pizza_sushi_steak.zip", "r") as zip_ref:
            zip_ref.extractall(IMAGE_PATH)
            print("Unzip complete...")
            print(f"Images contained in {IMAGE_PATH}")

## Transform PIL images to tensors
def data_transform():
    v2.Compose([
        v2.ToImage(),
        v2.Resize(size=(64, 64)),
        v2.RandomHorizontalFlip(p=0.5),
        v2.ToDtype(torch.float32, scale=True)
    ])


