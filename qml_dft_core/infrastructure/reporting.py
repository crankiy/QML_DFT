from __future__ import annotations

import csv
import json
from pathlib import Path


class TrainingReport:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = Path(output_dir)
        self.history_file = self.output_dir / "training_history.csv"
        self.summary_file = self.output_dir / "training_summary.json"
        self._init_history()

    def _init_history(self) -> None:
        if self.history_file.exists():
            return
        with self.history_file.open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["epoch", "learning_rate", "train_loss", "val_loss", "best_val_loss", "epoch_time_sec"])

    def append_epoch(self, epoch: int, learning_rate: float, train_loss: float, val_loss: float,
                     best_val_loss: float, epoch_time_sec: float) -> None:
        with self.history_file.open("a", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow([epoch, learning_rate, train_loss, val_loss, best_val_loss, epoch_time_sec])

    def write_summary(self, payload: dict) -> None:
        self.summary_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
