import os
from PIL import Image
from config import UPLOAD_DIR
import supervision as sv
from typing import List
import json


# Helper function to get list of uploaded files
def get_uploaded_files() -> List[str]:
    return [f for f in os.listdir(UPLOAD_DIR) if os.path.isfile(os.path.join(UPLOAD_DIR, f))]

# Helper function to get sv.Position from string
def get_position_from_string(position: str) -> sv.Position:
    positions = {
        "CENTER": sv.Position.CENTER,
        "CENTER_LEFT": sv.Position.CENTER_LEFT,
        "CENTER_RIGHT": sv.Position.CENTER_RIGHT,
        "TOP_CENTER": sv.Position.TOP_CENTER,
        "TOP_LEFT": sv.Position.TOP_LEFT,
        "TOP_RIGHT": sv.Position.TOP_RIGHT,
        "BOTTOM_LEFT": sv.Position.BOTTOM_LEFT,
        "BOTTOM_CENTER": sv.Position.BOTTOM_CENTER,
        "BOTTOM_RIGHT": sv.Position.BOTTOM_RIGHT
    }
    return positions.get(position.upper(), sv.Position.TOP_RIGHT)  # Default to TOP_RIGHT

def load_api_keys(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config
