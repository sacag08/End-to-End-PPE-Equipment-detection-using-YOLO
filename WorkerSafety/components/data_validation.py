import os,sys
import shutil
from workerSafety.logger import logging
from workerSafety.exception import CustomException
from workerSafety.entity.config_entity import DataValidationConfig
from workerSafety.entity.artifacts_entity import (DataIngestionArtifacts,
                                                 DataValidationArtifacts)

class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifacts,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise CustomException(e, sys)
        
    def validate_all_files_exist(self):
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in self.data_validation_config.required_file_list:
                if file not in all_files:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_validation(self) -> DataValidationArtifacts: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifacts(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                #copy the zip data in project folder for easy access
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd()) 

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)