import os,sys
from Credit_card.utils import get_collection_as_dataframe
from Credit_card.entity import config_entity
from Credit_card.entity.config_entity import DataIngestionConfig 
from Credit_card.entity.config_entity import TrainingPipelineConfig

from Credit_card.exception import Credit_cardException
from Credit_card.logger import logging
##from Credit_card.components import data_ingestion

if __name__=="__main__":
     try:
        ###get_collection_as_dataframe(database_name="bankcredits",collection_name="creaditcard")
         logging.info(f"Reading  training pipeline")
         training_pipeline_config=config_entity.TrainingPipelineConfig() 
         print(training_pipeline_config)
         dataingestion_config=config_entity.DataIngestionConfig      (training_pipeline_config=TrainingPipelineConfig)
         print(dataingestion_config.to_dict)
         #data_ingestion = DataIngestion(data_ingestion_config:config_entity.DataIngestionConfig)
         #print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
         raise Credit_cardException(e,sys) 
