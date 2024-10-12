import os, sys
from workerSafety.logger import logging
from workerSafety.exception import CustomException

from workerSafety.components.data_ingestion import DataIngestion
from workerSafety.components.data_validation import DataValidation
from workerSafety.components.model_trainer import ModelTrainer

from workerSafety.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifacts,ModelTrainerArtifacts
from workerSafety.entity.config_entity import DataIngestionConfig,DataValidationConfig,ModelTrainerConfig



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig
        self.data_validation_config = DataValidationConfig
        self.model_trainer_config = ModelTrainerConfig

    def start_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from the URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataValidationArtifacts:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def start_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e,sys)
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(
                data_ingestion_artifact= data_ingestion_artifact)
            if data_validation_artifacts.validation_status == True:
                    model_trainer_artifacts = self.start_model_trainer()
            else:
                raise Exception("Your data is not in correct format")
            
        except Exception as e:
            raise CustomException(e,sys)

