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
        self.csv_data_file_path: str = os.path.join(self.data_ingestion_artifacts_dir, CSV_DATA_FILE_NAME)


@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.data_transformation_artifacts_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.labels_to_ids_path: str = os.path.join(self.data_transformation_artifacts_dir, LABELS_TO_IDS_FILE_NAME)
        self.ids_to_labels_path: str = os.path.join(self.data_transformation_artifacts_dir, IDS_TO_LABELS_FILE_NAME)
        self.ids_to_labels_local_path: str = os.path.join(from_root(), IDS_TO_LABELS_FILE_NAME)
        self.df_train_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_TRAIN_FILE_NAME)
        self.df_val_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_VAL_FILE_NAME)
        self.df_test_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_TEST_FILE_NAME)
        self.unique_labels_path: str = os.path.join(self.data_transformation_artifacts_dir, UNIQUE_LABELS_FILE_NAME)


@dataclass
class ModelTrainingConfig:
    def __init__(self):
        self.model_training_artifacts_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_TRAINING_ARTIFACTS_DIR)
        self.bert_model_instance_path: str = os.path.join(self.model_training_artifacts_dir, GCP_MODEL_NAME)
        self.tokenizer_file_path: str = os.path.join(self.model_training_artifacts_dir, TOKENIZER_FILE_NAME)
        self.tokenizer_local_path: str = os.path.join(from_root(), TOKENIZER_FILE_NAME)


@dataclass
class ModelEvalConfig:
    def __init__(self):
        self.model_evaluation_artifacts_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_EVALUATION_ARTIFACTS_DIR)
        self.gcp_model_path: str = os.path.join(from_root())
        self.gcp_local_path: str = os.path.join(from_root(), GCP_MODEL_NAME)


@dataclass
class ModelPusherConfig:
    def __init__(self):
        self.bucket_name: str = BUCKET_NAME
        self.model_name: str = GCP_MODEL_NAME
        self.upload_model_path: str = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_TRAINING_ARTIFACTS_DIR)


@dataclass
class ModelPredictorConfig:
    def __init__(self):
        self.tokenizer_path: str = os.path.join(from_root(), TOKENIZER_FILE_NAME)
        self.ids_to_labels_path: str = os.path.join(from_root(), IDS_TO_LABELS_FILE_NAME)
        self.best_mdoel_dir: str = os.path.join(from_root(), BEST_MODEL_DIR)
        self.best_model_from_gcp_path: str = os.path.join(from_root(), BEST_MODEL_DIR)
        self.best_model_path: str = os.path.join(from_root(), BEST_MODEL_DIR, GCP_MODEL_NAME)