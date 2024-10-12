from workerSafety.logger import logging
from workerSafety.exception import CustomException
from workerSafety.pipeline.training_pipeline import TrainPipeline
import sys

obj = TrainPipeline()
obj.run_pipeline()
