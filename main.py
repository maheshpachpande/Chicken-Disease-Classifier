from CNNClassifier import logger
from CNNClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage03_training import ModelTrainingPipeline
from CNNClassifier.pipeline.stage04_evolution import EvolutionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    DataIngestionStage = DataIngestionTrainingPipeline()
    DataIngestionStage.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
except Exception as e:
    logger.exception(e)                
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    PrepareBaseModel = PrepareBaseModelTrainingPipeline()
    PrepareBaseModel.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
except Exception as e:
    logger.exception(e)                
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    Training = ModelTrainingPipeline()
    Training.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
except Exception as e:
    logger.exception(e)                
    raise e

STAGE_NAME = "Evolution"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    Training = EvolutionPipeline()
    Training.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
except Exception as e:
    logger.exception(e)                
    raise e