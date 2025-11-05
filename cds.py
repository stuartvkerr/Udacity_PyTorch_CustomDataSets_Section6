# This is the driver file
from imports import random, Image, plt, torch, v2
from tool_functions import get_images
from parameters import *

# Download images
#get_images()

# Get all image paths
image_path_list = list(IMAGE_PATH.glob("*/*/*.jpg"))
# Pick a random image path
random_image_path = random.choice(image_path_list)

print(random_image_path)

# Get the image class name using pathlib.Path.parent.stem
image_class = random_image_path.parent.stem

# Open image with Python's pillow (PIL fork)
img = Image.open(random_image_path)

# Show the image and print metadata
plt.imshow(img)
plt.title(f"Image class: {image_class}")
plt.axis(False) # hide axes
plt.show()

print(f"Random image path: {random_image_path}")
print(f"Image class: {image_class}")
print(f"Image height: {img.height}")
print(f"Image width: {img.width}")

data_transform = v2.Compose([
    v2.ToImage(),
    v2.Resize(size=(64, 64)),
    v2.RandomHorizontalFlip(p=0.5),
    v2.ToDtype(torch.float32, scale=True)
    ])

print(data_transform(img).shape)