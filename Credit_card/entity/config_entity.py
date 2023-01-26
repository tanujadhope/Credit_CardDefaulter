import logging
import os,sys
from datetime import datetime

from Credit_card.exception import Credit_cardException
from Credit_card.logger import logging

FILE_NAME="credit_default.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        try:
            logging.info(f"Reading OS path for training pipeline")
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
            os.makedirs(self.artifact_dir,exist_ok=True)
            #print(self.artifact_dir)
            logging.info(f"Reading OS path for training pipeline done")
        except Exception  as e:
             raise Credit_cardException(e,sys)   

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            logging.info(f"Reading OS path for dataingestion")
            self.database_name="bankcredits"
            self.collection_name="creaditcard" 
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
            logging.info(f"Reading OS path for dataingestion done")
        except Exception  as e:
            raise Credit_cardException(e,sys)     

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise Credit_cardException(e,sys)                

class DataValidationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir , "data_validation")
        self.report_file_path=os.path.join(self.data_validation_dir, "report.yaml")
        self.missing_threshold:float = 0.2
        self.base_file_path = os.path.join("default-of-credit-card-clients.csv")


class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...