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

# from ner.pipeline.prediction_pipeline import ModelPredictor

# mp = ModelPredictor()

# sen, label = mp.initiate_model_predictor(sentence='Bill Gates is the founder of Microsoft')

# print(sen)
# print(label)


from ner.pipeline.train_pipeline import TrainPipeline

tp = TrainPipeline()

tp.run_pipeline()


# Add API in the file and change permissions
# api:
#     auth_token: f0b6729453ac61769be5b9b5c4283013912680505fe24e526e201d0aa5f61cc0d4d199cd1793fb89

# runner:
#     name: dl-ineuron
#     working_directory: /var/opt/circleci/workdir
#     cleanup_working_directory: true




# [Unit]
# Description=CircleCI Runner
# After=network.target
# [Service]
# ExecStart=/opt/circleci/circleci-launch-agent --config /etc/opt/circleci/launch-agent-config.yaml
# Restart=always
# User=circleci
# NotifyAccess=exec
# TimeoutStopSec=18300
# [Install]
# WantedBy = multi-user.target