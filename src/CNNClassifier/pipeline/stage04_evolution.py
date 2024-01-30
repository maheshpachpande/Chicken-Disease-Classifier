from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.evolution import Evaluation
from CNNClassifier import logger
from CNNClassifier.components.prepare_callbacks import PrepareCallback

STAGE_NAME = 'EVOLUTION'

class EvolutionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        Evolution = EvolutionPipeline()
        Evolution.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==============================")
    except Exception as e:
        logger.exception(e)                
        raise e