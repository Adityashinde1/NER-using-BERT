# from ner.components.data_ingestion import DataIngestion
# from ner.components.data_transformation import DataTransformation
# from ner.components.model_training import ModelTraining
# from ner.components.model_evaluation import ModelEvaluation
# from ner.components.model_pusher import ModelPusher
# from ner.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvalConfig, ModelPusherConfig
# from ner.configuration.gcloud import GCloud

# if __name__ == '__main__': 

#     data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(), gcloud=GCloud())
#     data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

#     data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts)
#     data_transformation_artifacts = data_transformation.initiate_data_transformation()

#     model_training = ModelTraining(model_trainer_config=ModelTrainingConfig(), data_transformation_artifacts=data_transformation_artifacts)
#     model_trainer_artifacts = model_training.initiate_model_training()

#     model_eval = ModelEvaluation(data_transformation_artifacts=data_transformation_artifacts, model_training_artifacts=model_trainer_artifacts, 
#                                     model_evaluation_config=ModelEvalConfig())
#     model_eval_artifact = model_eval.initiate_model_evaluation()

#     model_pusher = ModelPusher(model_evaluation_artifact=model_eval_artifact, model_pusher_config=ModelPusherConfig())
#     model_pusher.initiate_model_pusher()

from ner.pipeline.prediction_pipeline import ModelPredictor

mp = ModelPredictor()

sen, label = mp.initiate_model_predictor(sentence='Bill Gates is the founder of Microsoft')

print(sen)
print(label)