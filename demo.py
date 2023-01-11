from ner.components.data_ingestion import DataIngestion
from ner.entity.config_entity import DataIngestionConfig
from ner.configuration.gcloud import GCloud


data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(), gcloud=GCloud())

data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()