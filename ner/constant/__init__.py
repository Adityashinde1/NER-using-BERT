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
CSV_DATA_FILE_NAME = 'ner.csv'

DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'

DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
LABELS_TO_IDS_FILE_NAME = 'labels_to_ids.pkl'
IDS_TO_LABELS_FILE_NAME = 'ids_to_labels.pkl'
DF_TRAIN_FILE_NAME = 'df_train.pkl'
DF_VAL_FILE_NAME = 'df_val.pkl'
DF_TEST_FILE_NAME = 'df_test.pkl'