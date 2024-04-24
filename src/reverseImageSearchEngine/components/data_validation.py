import os
import sys
from reverseImageSearchEngine.logger import logging
from reverseImageSearchEngine.exception import AppException
from reverseImageSearchEngine.utils import create_directories
from reverseImageSearchEngine.entity.config_entity import (DataIngestionConfig, 
                                                           DataValidationConfig)

class DataValidation:
    def __init__(self, data_config: DataValidation, validation_config: DataIngestionConfig):
        try:
            self.data_config = data_config
            self.validation_config = validation_config
        except Exception as e:
            raise AppException(e, sys)
        
        def validate_all_files_exist(self) -> bool:
            try:
                validation_status = None
                
                all_files = os.listdir(str(self.data_config.root_dir))
                
                for file in all_files:
                    if file not in self.validation_config.required_files:
                        validation_status=False
                        create_directories([self.validation_config.root_dir])
                        with open(self.validation_config.status_file_path, "w") as f:
                            f.write(f"Validation_status: {validation_status}")
                    else:
                        validation_status=True
                        create_directories([self.validation_config.root_dir])
                        with open(self.validation_config.status_file_path, "w") as f:
                            f.write(f"Validation_satus: {validation_status}")
            except Exception as e:
                raise AppException(e, sys)