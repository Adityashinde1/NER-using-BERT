import os
import sys
import logging
import numpy as np
import pandas as pd
from pandas import DataFrame
from ner.utils.utils import MainUtils
from ner.exception import NerException
from ner.entity.config_entity import DataTransformationConfig
from ner.entity.artifacts_entity import DataIngestionArtifacts, DataTransformationArtifacts

logger = logging.getLogger(__name__)

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts: DataIngestionArtifacts) -> None:
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.utils = MainUtils()

    def splitting_data(self, df: DataFrame):
        logger.info("Entered the splitting_data method of Data transformation class")
        try:
            df = df[0:1000]

            labels = [i.split() for i in df['labels'].values.tolist()]
            unique_labels = set()

            for lb in labels:
                    [unique_labels.add(i) for i in lb if i not in unique_labels]
            labels_to_ids = {k: v for v, k in enumerate(unique_labels)}
            ids_to_labels = {v: k for v, k in enumerate(unique_labels)}

            df_train, df_val, df_test = np.split(df.sample(frac=1, random_state=42),
                                        [int(.8 * len(df)), int(.9 * len(df))])

            logger.info("Exited the splitting_data method of Data transformation class")
            return labels_to_ids, ids_to_labels, df_train, df_val, df_test

        except Exception as e:
            raise NerException(e, sys) from e 


    # @ staticmethod
    # def align_label(texts, labels, tokenizer, labels_to_ids):
    #     try:
    #         label_all_tokens = False

    #         tokenized_inputs = tokenizer(texts, padding='max_length', max_length=512, truncation=True)
    #         word_ids = tokenized_inputs.word_ids()

    #         previous_word_idx = None
    #         label_ids = []

    #         for word_idx in word_ids:
    #             if word_idx is None:
    #                 label_ids.append(-100)

    #             elif word_idx != previous_word_idx:
    #                 try:
    #                     label_ids.append(labels_to_ids[labels[word_idx]])
    #                 except:
    #                     label_ids.append(-100)
    #             else:
    #                 try:
    #                     label_ids.append(labels_to_ids[labels[word_idx]] if label_all_tokens else -100)
    #                 except:
    #                     label_ids.append(-100)
    #             previous_word_idx = word_idx

    #         return label_ids

    #     except Exception as e:
    #         raise NerException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        logger.info("Entered the initiate_data_transformation method of Data transformation class")
        try:
            os.makedirs(self.data_transformation_config.data_transformation_artifacts_dir, exist_ok=True)
            logger.info(
                f"Created {os.path.basename(self.data_transformation_config.data_transformation_artifacts_dir)} directory."
            ) 

            df = pd.read_csv(self.data_ingestion_artifacts.csv_data_file_path)
            labels_to_ids, ids_to_labels, df_train, df_val, df_test = self.splitting_data(df=df)
            logger.info("Splitted the data")
            
            self.utils.dump_pickle_file(output_filepath=self.data_transformation_config.labels_to_ids_path, data=labels_to_ids)
            logger.info(f"Saved the labels to ids pickle file to Artifacts directory. File name - {os.path.basename(self.data_transformation_config.labels_to_ids_path)}")

            self.utils.dump_pickle_file(output_filepath=self.data_transformation_config.ids_to_labels_path, data=ids_to_labels)
            logger.info(f"Saved the ids to labels pickle file to Artifacts directory. File name - {os.path.basename(self.data_transformation_config.ids_to_labels_path)}")

            self.utils.dump_pickle_file(output_filepath=self.data_transformation_config.df_train_path, data=df_train)
            logger.info(f"Saved the train df pickle file to Artifacts directory. File name - {os.path.basename(self.data_transformation_config.df_train_path)}")

            self.utils.dump_pickle_file(output_filepath=self.data_transformation_config.df_val_path, data=df_val)
            logger.info(f"Saved the val df pickle file to Artifacts directory. File name - {os.path.basename(self.data_transformation_config.df_val_path)}")

            self.utils.dump_pickle_file(output_filepath=self.data_transformation_config.df_test_path, data=df_test)
            logger.info(f"Saved the test df pickle file to Artifacts directory. File name - {os.path.basename(self.data_transformation_config.df_test_path)}")

            data_transformation_artifacts = DataTransformationArtifacts(labels_to_ids_path=self.data_transformation_config.labels_to_ids_path,
                                                                        ids_to_labels_path=self.data_transformation_config.ids_to_labels_path,
                                                                        df_train_path=self.data_transformation_config.df_train_path,
                                                                        df_val_path=self.data_transformation_config.df_val_path,
                                                                        df_test_path=self.data_transformation_config.df_test_path)

            return data_transformation_artifacts

        except Exception as e:
            raise NerException(e, sys) from e 