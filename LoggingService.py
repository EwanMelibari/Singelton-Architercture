import logging
import sys

# Singleton Architecture - Logging Service
# Still working on it :)

class LoggingService:
    _instance = None

    def __new__(cls, log_file='app.log', log_level=logging.INFO):
        # Check if an instance exists
        if cls._instance is None:
            # If not, create a new instance
            cls._instance = super(LoggingService, cls).__new__(cls)
            
            # Perform one-time setup only on the first creation
            cls._instance._logger = logging.getLogger(__name__)
            cls._instance._logger.setLevel(log_level)

            # Check if handlers are already set (to prevent duplicate logs)
            if not cls._instance._logger.handlers:
                # Console Handler 
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setFormatter(
                    logging.Formatter(
                        '%(asctime)s - %(levelname)s - %(message)s'
                    )
                )
                cls._instance._logger.addHandler(console_handler)

                # File Handler 
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(
                    logging.Formatter(
                        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )
                )
                cls._instance._logger.addHandler(file_handler)

        return cls._instance

    def debug(self, message):
        pass

    def error(self, message):
        pass

    def info(self, message):
        pass

    def warning(self, message):
        pass

    def critical(self, message):
        pass