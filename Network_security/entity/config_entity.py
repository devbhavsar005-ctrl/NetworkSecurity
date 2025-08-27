from datetime import datetime
import os 
import sys 
from Network_security.constants import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%d_%m_%y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifacts_name=training_pipeline.ARTIFACT_DIR
        self.artifacts_dir=os.path.join(self.artifacts_name,timestamp)
        self.model_dir=os.path.join("final_model")
        self.timestamp:str=timestamp

class DataIngestionConfig:
    def __init__(self,training_piptlinr_config=TrainingPipelineConfig):
        self.data_ingestion_dir=os.path.join(
            training_piptlinr_config.artifacts_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )   
        self.feature_store_file_path=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FETAURE_STORE_DIR,training_pipeline.FILE_NAME
        )     
        self.training_file_path=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
        )

        self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME
