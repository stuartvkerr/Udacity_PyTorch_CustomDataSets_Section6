import torch
from torch import nn
from torch.utils.data import DataLoader

# Import torchvision
import torchvision
from torchvision import datasets
# from torchvision.transforms import ToTensor
from torchvision.transforms import v2


from torchmetrics import Accuracy
from torchmetrics.classification import MulticlassConfusionMatrix, ConfusionMatrix
from mlxtend.plotting import plot_confusion_matrix

# Import matplotlib for visualization
import matplotlib.pyplot as plt

import requests
import random
import zipfile
from pathlib import Path
import os

from PIL import Image

# device independence
device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)