import random
import json
from pathlib import Path

import numpy as np
import torch


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def save_json(obj: dict, path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)


def load_json(path: str | Path) -> dict:
    with open(path) as f:
        return json.load(f)


CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]


DISPLAY_NAMES = [
    "Pepper: Bacterial Spot",
    "Pepper: Healthy",
    "Potato: Early Blight",
    "Potato: Late Blight",
    "Potato: Healthy",
    "Tomato: Bacterial Spot",
    "Tomato: Early Blight",
    "Tomato: Late Blight",
    "Tomato: Leaf Mold",
    "Tomato: Septoria Leaf Spot",
    "Tomato: Spider Mites",
    "Tomato: Target Spot",
    "Tomato: Yellow Leaf Curl Virus",
    "Tomato: Mosaic Virus",
    "Tomato: Healthy",
]