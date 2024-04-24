from pathlib import Path
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: Path
    target: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file_path: Path
    required_files: list