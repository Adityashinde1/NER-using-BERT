from ner.components.data_ingestion import DataIngestion
from ner.components.data_transformation import DataTransformation
from ner.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from ner.configuration.gcloud import GCloud


data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(), gcloud=GCloud())

data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts)

data_transformation_artifacts = data_transformation.initiate_data_transformation()


