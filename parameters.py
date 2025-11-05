from imports import Path

## Parameters to load and process raw images
RAW_IMAGE_SOURCE = "https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip"
FOLDER_NAME = "data/"
IMAGE_FOLDER_NAME = "pizza_sushi_steak"

# make DATA_PATH a pathlib Path object
DATA_PATH = Path(FOLDER_NAME)
IMAGE_PATH = DATA_PATH / IMAGE_FOLDER_NAME


