ARTIFACTS_DIR: str = "artifacts"

"""
DATA INFESTION related constants for Data Ingestion VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/106pcsr6PSIdes0gHC0yD0M8ljHQCqDLL/view?usp=sharing"


"""
Data Validation related constants started with DATA_VAlIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train","test","data.yaml"]


"""
Model training related constants starts with MODEL_TRAINER VAR NAMES
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 50

MODEL_TRAINER_BATCH_SIZE: int = 16