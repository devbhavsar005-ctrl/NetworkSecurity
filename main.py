from Network_security.logging.logger import logging 
from Network_security.exception.exception import NetworkSecurityException

from Network_security.components.data_ingestion import DataIngestion
from Network_security.entity.artifacts_entity import DataIngestionArtifact
from Network_security.entity.config_entity import DataIngestionConfig
from Network_security.constants import training_pipeline
from Network_security.entity.config_entity import TrainingPipelineConfig

import sys 

if __name__=="__main__":
    try:

        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifacts=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifacts)

    except Exception as e:
        raise NetworkSecurityException(e,sys)    