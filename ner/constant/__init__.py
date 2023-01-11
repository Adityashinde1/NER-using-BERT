import os
from datetime import datetime
from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join(from_root(), "artifacts", TIMESTAMP)
LOGS_DIR = 'logs'
LOGS_FILE_NAME = 'ner.log' 
MODELS_DIR = 'models'

BUCKET_NAME = 'ner-using-bert'
GCP_DATA_FILE_NAME = 'archive.zip'

DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'
