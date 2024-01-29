from CNNClassifier import logger
from CNNClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
except Exception as e:
    logger.exception(e)                
    raise e

logger.info("Welcome")