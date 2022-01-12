import os 
import sys

ROOT_DIR = os.path.abspath("..")

print(ROOT_DIR)

sys.path.append(ROOT_DIR)

from mrcnn import model
from mrcnn import visualize
from mrcnn.config import Config