from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class DatasetSplit:
    train_indices: list[int]
    val_indices: list[int]
    test_indices: list[int]

    @property
    def train_size(self) -> int:
        return len(self.train_indices)

    @property
    def val_size(self) -> int:
        return len(self.val_indices)

    @property
    def test_size(self) -> int:
        return len(self.test_indices)


def build_dataset_split(dataset_size: int, train_ratio: float, val_ratio: float, test_ratio: float, seed: int) -> DatasetSplit:
    train_size = int(train_ratio * dataset_size)
    val_size = int(val_ratio * dataset_size)
    test_size = int(test_ratio * dataset_size)
    if train_size + val_size + test_size > dataset_size:
        raise ValueError("Split sizes exceed dataset size")
    indices = list(range(dataset_size))
    rng = np.random.default_rng(seed)
    rng.shuffle(indices)
    return DatasetSplit(
        train_indices=indices[:train_size],
        val_indices=indices[train_size:train_size + val_size],
        test_indices=indices[train_size + val_size:train_size + val_size + test_size],
    )


def save_dataset_split(split: DatasetSplit, output_dir: str) -> Path:
    target = Path(output_dir) / "dataset_split.json"
    payload = {
        "train_indices": split.train_indices,
        "val_indices": split.val_indices,
        "test_indices": split.test_indices,
        "train_size": split.train_size,
        "val_size": split.val_size,
        "test_size": split.test_size,
    }
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return target
