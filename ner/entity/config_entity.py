from dataclasses import dataclass
from from_root import from_root
import os
from ner.constant import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.data_ingestion_artifacts_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.gcp_data_file_path: str = os.path.join(self.data_ingestion_artifacts_dir, GCP_DATA_FILE_NAME)
        self.output_file_path: str = os.path.join(self.data_ingestion_artifacts_dir)